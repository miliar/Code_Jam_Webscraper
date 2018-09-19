#-------------------------------------------------------------------------------
# Name:        gcj 2011 q-a
# Purpose:
# Created:     07/05/2011
# Copyright:   (c)  2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys


def movecount(seq):
    pos_o = 1
    pos_b = 1
    next_o,next_b =[],[]
    cnt = 0
    for s in seq:
        if s[0] == "O":
            next_o.append(s[1])
        else:
            next_b.append(s[1])

    #初期距離設定
    if len(next_o) > 0:
        dis_o = abs(next_o[0] - pos_o)
    else:
        dis_o = 0
    if len(next_b) > 0:
        dis_b = abs(next_b[0] - pos_b)
    else:
        dis_b = 0

    for i in range(len(seq)):
        if seq[i][0] == "O":
            cnt += dis_o + 1 #move + push
            pos_o = next_o.pop(0)

            if dis_o + 1 < dis_b:
                dis_b = dis_b - 1 - dis_o
            else:
                dis_b = 0
            if len(next_o) > 0:
                dis_o = abs(next_o[0] - pos_o)
            else:
                dis_o = 0
        if seq[i][0] == "B":
            cnt += dis_b + 1 #move + push
            pos_b = next_b.pop(0)

            if dis_b + 1 < dis_o:
                dis_o = dis_o - 1 - dis_b
            else:
                dis_o = 0
            if len(next_b) > 0:
                dis_b = abs(next_b[0] - pos_b)
            else:
                dis_b = 0
    return cnt

def main():
    f = open(sys.argv[1])
    fo = open(sys.argv[2],"w")

    line = f.readline()
    cases = int(line.strip())
    for i in range(cases):
        l = f.readline().strip().split()
        buttons = int(l[0])
        seq = []
        for n in range(buttons):
            r,b = l[n*2+1],int(l[n*2+2]) #robot,button
            seq.append([r,b])
        out = "Case #%d: "%(i+1) + str(movecount(seq)) + "\n"
        print out,
        fo.write(out)

    f.close()
    fo.close()

if __name__ == '__main__':
    main()
