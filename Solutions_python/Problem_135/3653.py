#!/usr/bin/env python

N=int(raw_input())
for i in range(N):
    row1=int(raw_input())
    for r in range(1,5):
        row = map(int, raw_input().split(" "))
        if r == row1:
            set1 = set(row)
    row2=int(raw_input())
    for r in range(1,5):
        row = map(int, raw_input().split(" "))
        if r == row2:
            set2 = set(row)
    #print row1,row2,set1,set2
    ans = set1.intersection(set2)
    if len(ans) == 1:
        res = str(ans.pop())
    elif len(ans) == 0:
        res = "Volunteer cheated!"
    else:
        res = "Bad magician!"
    print "Case #%d: %s" %(i+1, res)
