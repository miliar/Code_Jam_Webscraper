import sys
import os

if __name__ == '__main__':

    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        first = int(sys.stdin.readline())
        fm = []
        for j in xrange(4):
            fm.append([int(num) for num in sys.stdin.readline().split()])


        second = int(sys.stdin.readline())
        sm = []
        for j in xrange(4):
            sm.append([int(num) for num in sys.stdin.readline().split()])
        
        #sys.stdout.write('Case #{0}: {1}\n'.format(i+1, total))
    
        res = set(fm[first-1]).intersection(set(sm[second-1]))

        if len(res) == 0:
            sys.stdout.write('Case #{0}: {1}\n'.format(i+1, "Volunteer cheated!"))
        elif len(res) == 1:
            sys.stdout.write('Case #{0}: {1}\n'.format(i+1, res.pop()))
        else:
            sys.stdout.write('Case #{0}: {1}\n'.format(i+1, "Bad magician!"))

        #print first
        #print fm
        #print second
        #print sm
            
                


