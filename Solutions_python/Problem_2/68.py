#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from __future__ import with_statement

from optparse import OptionParser
import sys
import re

parser = OptionParser()
parser.add_option("-d", "--debug", action="store_true", dest="debug")

(options, args) = parser.parse_args()

def decorator(old_decorator):
    "Restore original name, doc & dict for decorated functions"
    def new_decorator(f):
        g = old_decorator(f)
        g.__name__ = f.__name__
        g.__doc__ = f.__doc__
        g.__dict__.update(f.__dict__)
        return g

    new_decorator.__name__ = old_decorator.__name__
    new_decorator.__doc__ = old_decorator.__doc__
    new_decorator.__dict__.update(old_decorator.__dict__)

    return new_decorator

def memoize(cache=None):
    """Decorator to memoize a function
    Can be used on multiple functions
    Warning: Does not reclaim memory"""

    if cache == None:
        cache = {}

    @decorator
    def m(f):
        def g(*args, **kwargs):
            key = ( f, tuple(args), frozenset(kwargs.items()) )
            if key not in cache:
                cache[key] = f(*args, **kwargs)
            return cache[key]

        return g

    return m

if args:
    input_filename = args[0]

    f = open(input_filename, 'r')

    num_tests = int(f.readline().strip())
    if options.debug:
        print "num_tests", num_tests

    for test in range(1, num_tests + 1):
        trips = []
        turnaround = int(f.readline().strip())

        line = f.readline().strip()
        match = re.search(r'^([0-9]+)\s+([0-9]+)\s*$', line)
        assert match, "A B not found: %s" % repr(line)
        len_a = int(match.group(1))
        len_b = int(match.group(2))

        for a in range(len_a):
            line = f.readline().strip()
            match = re.search(r'^([0-9]+):([0-9]+)\s+([0-9]+):([0-9]+)\s*$', line)
            assert match, "Bad time: %s" % repr(line)
            depart = int(match.group(1)) * 60 + int(match.group(2))
            arrive = int(match.group(3)) * 60 + int(match.group(4))
            trips.append((depart, arrive, 'a', 'b'))
        for b in range(len_b):
            line = f.readline().strip()
            match = re.search(r'^([0-9]+):([0-9]+)\s+([0-9]+):([0-9]+)\s*$', line)
            assert match, "Bad time: %s" % repr(line)
            depart = int(match.group(1)) * 60 + int(match.group(2))
            arrive = int(match.group(3)) * 60 + int(match.group(4))
            trips.append((depart, arrive, 'b', 'a'))
        trips.sort()

        if options.debug:
            print "Test", test
            print "  turn", turnaround
            print "  trips", repr(trips)

        trains = [] # [(station, availablefrom)
        trains_from = {'a' : 0, 'b': 0}

        for (depart, arrive, station_from, station_to) in trips:
            # allocate a train for this journey
            found = False
            for t in range(len(trains)):
                (station_at, available) = trains[t]
                if station_at == station_from and available <= depart:
                    trains[t] = (station_to, arrive + turnaround)
                    found = True
                    if options.debug:
                        print "Old train", t, station_from, depart, arrive, arrive + turnaround
                    break
            if not found:
                # Need a new train
                trains_from[station_from] += 1
                if options.debug:
                    print "New train", station_from, depart, arrive, arrive + turnaround
                trains.append((station_to, arrive + turnaround))

        print "Case #%s: %s %s" % (test, trains_from['a'], trains_from['b'])
