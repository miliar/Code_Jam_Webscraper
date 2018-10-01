#!/usr/bin/python

arg = 'sample'
ifn = './' + arg + '.txt'
ofn = './' + arg + '_ans.txt'


ifn = 'A-small-attempt0.in'
ofn = 'A-small-ans.txt'
ofp = open(ofn, 'w')

with open(ifn, 'r') as ifp:
        T = (int)(ifp.readline())
        for i in range(T):
                n1 = (int)(ifp.readline())
                for j in range(4):
                        if j == n1-1:
                                line = ifp.readline();
                                row1 = [int(p) for p in line.split(' ')]
                        else:
                                ifp.readline()
                n2 = (int)(ifp.readline())
                for j in range(4):
                        if j == n2-1:
                                line = ifp.readline();
                                row2 = [int(p) for p in line.split(' ')]
                        else:
                                ifp.readline()
                cnt = 0
                for x in row2:
                        if(x in row1):
                                cnt = cnt+1
                                num = x
                ofp.write("Case #%d: " % (i+1))
                if cnt ==  0:
                        ofp.write("Volunteer cheated!\n")
                elif cnt == 1:
                        ofp.write("%d\n" % num)
                else:
                        ofp.write("Bad magician!\n")
ifp.close()
ofp.close()
