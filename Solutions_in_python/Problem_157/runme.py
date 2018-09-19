#!/usr/bin/env python3
"""
Dijkstra problem
for Google Code Jam 2015
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/6224486/dashboard#s=p2

Author: 
  Chris Nitsas
  (nitsas)

Language:
  Python 3(.4)

Date:
  April, 2015

Usage:
  python3 runme.py input_file
"""


import sys
import argparse
from collections import namedtuple
# modules I've written:
from helpful import *


_program_description = \
'''TEMPLATE PROGRAM DESCRIPTION'''


_input_file_description = \
'''TEMPLATE INPUT FILE DESCRIPTION'''


TestCase = namedtuple('TestCase', ['L', 'X', 'pattern'])


def parse_args():
    """
    Parse the command line arguments and return them in a namespace.
    """
    parser = argparse.ArgumentParser(description=_program_description)
    parser.add_argument('input_file', help=_input_file_description)
    #parser.add_argument('-v', '--verbose', action='store_true', 
    #                    default=False, help='show progress')
    args = parser.parse_args()
    return args


class NoMoreFoodError(Exception):
    def __init__(self, msg=None):
        if msg is None:
            self.msg = 'out of food!'
        else:
            self.msg = msg
    def __str__(self):
        return str(self.msg)


_result_state = { '1':  { '1': '1', 
                          'i': 'i', 
                          'j': 'j', 
                          'k': 'k', 
                          '-1': '-1', 
                          '-i': '-i', 
                          '-j': '-j', 
                          '-k': '-k' }, 
                  'i':  { '1': 'i', 
                          'i': '-1', 
                          'j': 'k', 
                          'k': '-j', 
                          '-1': '-i', 
                          '-i': '1', 
                          '-j': '-k', 
                          '-k': 'j' }, 
                  'j':  { '1': 'j', 
                          'i': '-k', 
                          'j': '-1', 
                          'k': 'i', 
                          '-1': '-j', 
                          '-i': 'k', 
                          '-j': '1', 
                          '-k': '-i' }, 
                  'k':  { '1': 'k', 
                          'i': 'j', 
                          'j': '-i', 
                          'k': '-1', 
                          '-1': '-k', 
                          '-i': '-j', 
                          '-j': 'i', 
                          '-k': '1' }, 
                  '-1': { '1': '-1', 
                          'i': '-i', 
                          'j': '-j', 
                          'k': '-k', 
                          '-1': '1', 
                          '-i': 'i', 
                          '-j': 'j', 
                          '-k': 'k' }, 
                  '-i': { '1': '-i', 
                          'i': '1', 
                          'j': '-k', 
                          'k': 'j', 
                          '-1': 'i', 
                          '-i': '-1', 
                          '-j': 'k', 
                          '-k': '-j' }, 
                  '-j': { '1': '-j', 
                          'i': 'k', 
                          'j': '1', 
                          'k': '-i', 
                          '-1': 'j', 
                          '-i': '-k', 
                          '-j': '-1', 
                          '-k': 'i' }, 
                  '-k': { '1': '-k', 
                          'i': '-j', 
                          'j': 'i', 
                          'k': '1', 
                          '-1': 'k', 
                          '-i': 'j', 
                          '-j': '-i', 
                          '-k': '-1' } }


def _evaluate_food_sequence(food_sequence):
    eater = InsatiableEater()
    eater.eat_food_sequence(food_sequence)
    return eater.get_state()


def _raise_state_to_power(state, power):
    # (optimize this)
    assert(len(state) == 1 or len(state) == 2)
    if len(state) == 2:
        assert(state[0] == '-')
    # break the state down to parts:
    has_minus = (len(state) == 2)
    quaternion = state[-1]
    # what power do we raise it to? there are only 4 possible results
    if power % 4 == 0:
        return '1'
    elif power % 4 == 1:
        return state
    elif power % 4 == 2:
        if quaternion == '1':
            return '1'
        else:
            return '-1'
    elif power % 4 == 3:
        if quaternion == '1':
            return state
        else:
            if has_minus:
                return quaternion
            else:
                return '-' + quaternion
    # (optimize this)
    assert(False)


def _eat_and_change_state(state, food):
    eater = InsatiableEater(state)
    eater.eat_food_sequence([food])
    return eater.get_state()


class InsatiableEater:
    """
    The InsatiableEater will eat whole sequences of food.
    """
    def __init__(self, initial_state='1'):
        # initial state:
        self.state = initial_state
    
    def eat_food_sequence(self, food_sequence):
        for food in food_sequence:
            self.state = _result_state[self.state][food]
    
    def get_state(self):
        return self.state


class TargetEater:
    """
    The TargetEater will eat from a Feeder until it reaches a target state.
    
    Targets can only be 'i' or 'j' - for now.
    """
    def __init__(self, target, feeder):
        """
        Initialize everything.
        """
        # initial state:
        self.state = '1'
        # target state:
        assert(target == 'i' or target == 'j')
        self._target = target
        # the feeder:
        self._feeder = feeder
    
    def start_eating(self):
        """
        Eat from the feeder until you reach the target state.
        
        Careful: This will throw a NoMoreFoodError if the Feeder runs out.
        """
        while (self.state != self._target):
            self.state = _result_state[self.state][self._feeder.request_food()]
    
    def get_state(self):
        return self.state


class Feeder:
    """
    The Feeder will feed any eaters that request food until food runs out.
    
    It can also evaluate the food that's left over.
    """
    def __init__(self, pattern, times):
        # remember the (complete) pattern
        self._pattern = pattern
        self._times_left = times
        self._feed_stack = []
        self._refill_feed_stack()
    
    def _refill_feed_stack(self):
        """
        Refill the feed stack and decrement self._times_left. 
        
        It's a feed *stack* for performance reasons (fast pops from the end).
        
        Careful: This will throw NoMoreFoodError if there's no more food!
        """
        assert(len(self._feed_stack) == 0)
        if not self._times_left > 0:
            raise NoMoreFoodError()
        # refill the feed stack
        self._feed_stack = list(reversed(self._pattern))
        # used one of the times left (i.e. reserve repeats of the pattern) to
        # refill the feed stack
        self._times_left = self._times_left - 1
    
    def request_food(self):
        """
        Return the next piece of food (i.e. next letter).
        
        Careful: This will throw NoMoreFoodError if there's no more food!
        """
        try:
            return self._feed_stack.pop()
        except IndexError:
            # this next line will throw if there's no more food
            self._refill_feed_stack()
        return self._feed_stack.pop()
    
    def evaluate_leftovers(self):
        # evaluate the contents of the feed stack
        state = _evaluate_food_sequence(reversed(self._feed_stack))
        # evaluate the reserve repeats of the pattern
        if self._times_left > 0:
            # evaluate the whole pattern and then raise it to the power
            # `self._times_left`
            rest_of_state = _evaluate_food_sequence(self._pattern)
            rest_of_state = _raise_state_to_power(rest_of_state, 
                                                  self._times_left)
            state = _eat_and_change_state(state, rest_of_state)
        return state


def makes_ijk(test_case):
    feeder = Feeder(test_case.pattern, test_case.X)
    eater = TargetEater('i', feeder)
    try:
        eater.start_eating()
    except NoMoreFoodError:
        return 'NO'
    eater = TargetEater('j', feeder)
    try:
        eater.start_eating()
    except NoMoreFoodError:
        return 'NO'
    if feeder.evaluate_leftovers() == 'k':
        return 'YES'
    else:
        return 'NO'


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        T = read_int(f)
        test_cases = list()
        for i in range(T):
            L, X = read_list_of_int(f)
            pattern = f.readline().rstrip()
            test_cases.append(TestCase(L, X, pattern))
    for i, tc in enumerate(test_cases, start=1):
        print('Case #{}: {}'.format(i, makes_ijk(tc)))
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
