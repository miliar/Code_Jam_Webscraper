#!/usr/bin/python
import sys

def make2dList(rows, cols):
    a=[]
    for row in xrange(rows): a += [[0]*cols]
    return a


if __name__ == '__main__':
    grid = make2dList(4, 4)
    lines = list()
    with open(str(sys.argv[1]), 'r') as f:
        lines = f.readlines()
        ind = 1;
        cases = int(lines[0])
        for case in range(cases):
            sel1 = int(lines[ind])
            ind += sel1
            row1 = map(int, lines[ind].split())
            ind += (5 - sel1)

            sel2 = int(lines[ind])
            ind += sel2
            row2 = map(int, lines[ind].split())
            ind += (5 - sel2)
            count = 0
            cur_sel = 0;
            for num in row2:
                if num in row1:
                    cur_sel = num
                    count += 1
            result = ""
            if count == 0:
                result = "Volunteer cheated!"
            elif count == 1:
                result = cur_sel
            else:
                result = "Bad magician!"
            print 'Case #{:}: {:}'.format(case+1, result)






