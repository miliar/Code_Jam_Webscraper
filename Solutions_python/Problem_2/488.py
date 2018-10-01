#!/usr/bin/env python
import sys

def read(name="input"):
    name = sys.argv[1] if len(sys.argv) > 1 else name
    return [line.strip() for line in open(name).readlines()]

def bla(abs, bas):
    # = ([time I'll have a new train], how many I need thus far)
    a = ([], [0])
    b = ([], [0])
    abs = [(x, 'a') for x in abs]
    bas = [(x, 'b') for x in bas]
    for ((depart, arrive), where) in sorted(abs + bas):
        (times, needed), (other, _) = (a,b) if where == 'a' else (b,a)
        if not times or depart < times[0]: # we'll need a train
            needed[0] += 1
        else:
            times.pop(0)
        other.append(arrive)
        other.sort()
    return a[1][0], b[1][0]

def main():
    input = read()
    def foo():
        return int(input.pop(0))
    def bar():
        return map(int, input.pop(0).split())
    def add_turn(xs):
        def hour(n):
            x = n % 100
            return n if x < 60 else n + 40
        return sorted((x, hour(y + turnaround)) for x,y in xs)
    cases = foo()
    for case in range(cases):
        print "Case #%d:" % (case + 1),
        turnaround = foo()
        na, nb = bar()
        ab, input = input[:na], input[na:]
        ba, input = input[:nb], input[nb:]
        print "%d %d" % bla(*map(add_turn, map(reader, [ab, ba])))

def reader(xs):
    # holy moly
    return (tuple(map(int, ''.join(x.split(':')).split())) for x in xs)


if __name__ == '__main__':
    main()
