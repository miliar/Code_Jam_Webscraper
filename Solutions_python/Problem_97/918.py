#!/usr/bin/env python
from sys import stdin 

def check_recycled(lb, ub):
    #print lb + '---' + ub
    count = 0
    lb = int(lb)
    ub = int(ub)
    while lb <= ub:
        lbchars = str(lb)
        lbchars = [c for c in lbchars]
        r = range(len(lbchars))
        r.reverse()
        r.pop()
        checked = set()
        for index in r:
            perm = lbchars[index:]
            perm.extend(lbchars[:index])
            perm = ''.join(perm)
            m = int(perm)
            if m > lb and m <= ub and (lb, m) not in checked:
                count+=1
                checked.add((lb, m))
        lb+=1
    return count

def main():
    no_cases = int(stdin.readline())
    for case in range(no_cases):
        lb, ub = stdin.readline().split()
        count = check_recycled(lb, ub)
        print 'Case #%d: %d' % (case+1, count)

if __name__ == '__main__':
    main()
