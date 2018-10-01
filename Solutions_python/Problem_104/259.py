#!/usr/bin/python

import sys, itertools

def solve(input):

    sums=dict()
    for i in range(len(input)):
        for subset in set(itertools.combinations(input, i)):
            if sum(subset) in sums:
                return sums[sum(subset)], subset
            sums[sum(subset)]=subset
    return 'Impossible'

if __name__ == '__main__':
    with open(sys.argv[2], 'w') as out:
        with open(sys.argv[1]) as f:
            for i in range(int(f.readline())):
                input=tuple(map(int, f.readline().split()))
                result=solve(input[1:])
                print('Case #{}:'.format(i+1), file=out)
                if result=='Impossible':
                    print(result)
                else:
                    print(*result[0], file=out)
                    print(*result[1], file=out)
