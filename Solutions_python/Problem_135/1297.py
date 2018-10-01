#!/usr/bin/en python
import sys

if __name__ == '__main__':
    fh = file(sys.argv[1], 'r')
    n = int(fh.readline())
    for i in range(n):
        # Get rows
        v1 = fh.readline().split()[0]
        for j in range(4):
            temp = fh.readline()
            if j+1 == int(v1):
                row1 = temp.split()
        v2 = fh.readline().split()[0]
        for j in range(4):
            temp = fh.readline()
            if j+1 == int(v2):
                row2 = temp.split()
        
        # Process coincidences
        res = None
        for v in row1:
            if v in row2:
                if res is None:
                    res = v
                else:
                    res = 'bad'
                    
        # Print result
        if res is None:
            print 'Case #%d: Volunteer cheated!' % (i+1)
        elif res == 'bad':
            print 'Case #%d: Bad magician!' % (i+1)
        else:
            print 'Case #%d: %s' % (i+1, res)
