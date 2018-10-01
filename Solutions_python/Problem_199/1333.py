#!/usr/bin/env python3

import logging
import math
import sys

logger = logging.getLogger()
#logging.basicConfig(level=logging.DEBUG, 
#        stream=sys.stderr, format='CJ15.QR.B %(levelname)s %(message)s')

def problem_cases():
    num_cases_total = -1
    num_cases_passed = 0
    
    for count, line in enumerate(sys.stdin):
        line = line.rstrip()
        
        if count == 0:
            num_cases_total = int(line)
            logger.debug('{} cases in total.'.format(num_cases_total))
            continue
        
        current_case, flip_size = line.split(' ')
        current_case = current_case.replace('-', '0').replace('+', '1')
        flip_size = int(flip_size)

        num_cases_passed += 1
        logging.debug('Case #{} {} (flip size={})'.format(
        num_cases_passed, current_case, flip_size))
        
        yield (count, current_case, flip_size)
    
    assert num_cases_passed == num_cases_total
    

def solve(pancakes_sides, flip_size):
    last_position = len(pancakes_sides) - flip_size
    num_flips = 0

    try:
        flip_position = pancakes_sides.index('0')
    except:
        logger.debug('{} => ALL OK!'.format(pancakes_sides))
        return 0;

    while flip_position <= last_position:
        flip_mask = '0'*flip_position + '1'*flip_size + '0'*(len(pancakes_sides) - flip_position - flip_size)
        pancakes_sides = bin(int(pancakes_sides, 2)^int(flip_mask, 2))[2:]
        num_flips += 1
        
        logger.debug('current state: {}'.format(pancakes_sides))
        logger.debug('         mask: {}'.format(flip_mask))
        logger.debug('       result: {}\n'.format(pancakes_sides))

        try:
            flip_position = pancakes_sides.index('0')
        except:
            logger.debug('All pancakes happy side up in {} flips'.format(num_flips))
            return num_flips

    return 'IMPOSSIBLE'

        
    
if __name__ == '__main__':
    print('GOOGLE CODEJAM 2017 - Qualification Round - Problem A', file=sys.stderr)
    for case_id, case, flip_size in problem_cases():
        solution = solve(case, flip_size)
        print('Case #{}: {}'.format(case_id, solution))
        

