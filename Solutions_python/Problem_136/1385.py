
from __future__ import division

import sys
from collections import Counter
import itertools
from pprint import pprint





def write_output(output):
    lines = []
    for i, out in enumerate(output):
        line = 'Case #{}: {:.07f}'.format(i + 1, out)
        lines.append(line)

    txt = '\n'.join(lines) + '\n'
    with open(r'C:\codejam\output.txt', 'w') as f:
        f.write(txt)


def process(c, f, x):
    min_cookie_time = None
    num_farms = 0

    while True:
        cookie_time = get_cookie_time(c, f, x, num_farms)
        if min_cookie_time is None or cookie_time < min_cookie_time:
            min_cookie_time = cookie_time
            num_farms += 1
        else:
            return min_cookie_time
        
    


def get_cookie_time(c, f, x, num_farms):
    rate = f * num_farms + 2.0
    secs = x / rate    
    return secs + farm_time(c, f, x, num_farms)


cache = {}

def farm_time(c, f, x, num_farms):
    if num_farms == 0:
        cache[(c, f, x, num_farms)] = 0
        return 0
    
    rate = f * (num_farms - 1) + 2.0
    secs = c / rate + cache.get((c, f, x, num_farms - 1))
    cache[(c, f, x, num_farms)] = secs
    return secs


def main():
    output = []

    filepath = r'C:\codejam\input.txt'
    with open(filepath, 'r') as fi:
        num_cases = int(fi.readline().strip())
        for i in range(num_cases):
            c, f, x = map(float, fi.readline().strip().split())


            output.append(process(c, f, x))

    write_output(output)


if __name__ == '__main__':
    main()