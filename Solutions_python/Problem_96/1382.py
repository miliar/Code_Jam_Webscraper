#!/usr/bin/python

import sys

def solve(input):
    n, s, p, *googlers = list(map(int, input.split()))
    count=0
    for googler in googlers:
        if s>0 and max(p,p*3-4)<=googler<p*3-2:
            count+=1
            s-=1
        elif max(p,p*3-2)<=googler:
            count+=1
    return count

if __name__ == '__main__':
    with open(sys.argv[2], 'w') as out:
        with open(sys.argv[1]) as f:
            n = int(f.readline())
            for i, input in enumerate(f):
                input=input.strip()
                result=solve(input.strip())
                print('Case #{}: {}'.format(i+1,result), file=out)

