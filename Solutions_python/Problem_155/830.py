#!/usr/bin/python3
from sys import argv

def solve(n, audience):
    sum = 0
    friends = 0
    for (i, x) in enumerate(audience):
        newX = 0
        if i > sum:
            newX = i - sum
            friends = friends + newX

        sum += newX + x
            
    return friends

def main(args):
    with open(args[1]) as inp, open(args[2], 'w') as out:
        cases = int(inp.readline())
        for case in range(cases):
            n, audience = inp.readline().split()
            n = int(n)
            audience = [int(x) for x in audience]
            friends = solve(n, audience)

            out.write("Case #%d: %d\n" % ((case + 1), friends))

if __name__ == '__main__':
    main(argv)
