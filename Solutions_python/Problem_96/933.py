#!/usr/bin/env python
from sys import stdin

def find_max_count(scores, minscore, surprises):
    count = 0
    if minscore == 0:
        return len(scores)
    for score in scores:
        rem = score - minscore
        if rem >= ((minscore-1)*2) and (minscore-1 >= 0):
            count+=1
            continue
        elif rem >= ((minscore-2)*2) and surprises > 0 and (minscore-2 >= 0):
            count+=1
            surprises-=1
            continue
    return count

def main():
    no_cases = int(stdin.readline())
    for case in range(no_cases):
        data = stdin.readline().split()
        data = map(int, data)
        data.reverse()
        no_dancers = data.pop()
        no_surprises = data.pop()
        minscore = data.pop()
        scores = data
        count = find_max_count(scores, minscore, no_surprises)
        print 'Case #%d: %d' % (case+1, count)

if __name__ == '__main__':
    main()
