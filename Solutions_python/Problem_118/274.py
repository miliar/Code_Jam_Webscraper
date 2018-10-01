#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import math
import time
from itertools import product

def is_palindrome(number):
    strnum = str(number)
    middle, mod = divmod(len(strnum), 2)
    return strnum[:middle] == strnum[middle+mod:][::-1]

class Solver(object):
    limits = []
    
    def check_and_save(self, number):
        if is_palindrome(number**2):
            self.storage.write('%d\n' % number)
            self.storage.flush()

    def solve_and_store(self):
        start_digits = ('1', '2')
        end_digits = ('0', '1', '2')
        one_zero = ('0', '1')
        with open('cache.txt', 'wt') as storage:
            self.storage = storage
            for number_of_digits in range(1, 51):
                if number_of_digits == 1:
                    for number in [1, 2, 3]:
                        self.check_and_save(number)
                else:
                    div, mod = divmod(number_of_digits, 2)
                    if mod == 0:
                        digits = [start_digits] + [one_zero for i in range(div-1)]
                    else:
                        digits = [start_digits] + [one_zero for i in range(div-1)] + [end_digits]
                    for item in product(*digits):
                        if mod == 0:
                            number = ''.join(item + item[::-1])
                        else:
                            number = ''.join(item + item[:-1][::-1])
                        self.check_and_save(int(number))

    def load_solved(self):
        with open('cache.txt', 'rt') as storage:
            start = time.time()
            self.numbers = [int(line.rstrip())**2 for line in storage.readlines()]
        
    def count_in_limit(self, a, b):
        return len([item for item in self.numbers if a <= item <= b])
    
    def add_limit(self, limit):
        self.limits.append(limit)
        
    def print_result(self):
        for index, limit in enumerate(self.limits):
            result = self.count_in_limit(*limit)
            print('Case #{0}: {1}'.format(index+1, result))

def handle_input(source):
    number = int(next(source).strip())
    solver = Solver()
    solver.load_solved()
    for index in range(number):
        line = next(source).strip()
        limit = map(int, line.split(' '))
        solver.add_limit(limit)
    solver.print_result()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'presolve':
        solver = Solver()
        solver.solve_and_store()
    else:
        handle_input(sys.stdin)
