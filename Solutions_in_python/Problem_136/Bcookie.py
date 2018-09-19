#!/usr/bin/python3

from sys import argv

def answer(c,f,x):
    seconds = 0
    cookieRate = 2
    best = float('inf')
    while True:
        # Could finish at this time without buying more farms
        couldFinish = seconds + x / cookieRate
        if best > couldFinish:
            best = couldFinish
        else:
            break
        # Now try buying another farm and see if it helps; if not, stop buying farms
        seconds += c / cookieRate
        cookieRate += f
    return best

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Google Code Jam I/O
    infile = open(argv[1])
    cases = int(infile.readline())
    for i in range(cases):
        c,f,x = map(float, infile.readline().split())
        print('Case #{}: {:.7f}'.format(i+1, answer(c,f,x)))
