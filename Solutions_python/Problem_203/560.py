from collections import *
from math import *
from itertools import *
from string import ascii_uppercase

def check(a):
    for i in a:
        if '?' in i:
            return True
    return False

def rowwise(a,r,c):
    ans = a[:]
    for i in range(r):
        for j in range(c):
            if a[i][j]=='?':
                ti = j
                tj = j
                while ti>=0:
                    if a[i][ti]!='?':
                        ans[i][j] = a[i][ti]
                        break
                    ti-=1
                if ans[i][j]=='?':
                    while tj<c:
                        if a[i][tj]!='?':
                            ans[i][j] = a[i][tj]
                            break
                        tj+=1
            #print i,j,ans
    return ans

def colwise(a,r,c):
    ans = a[:]
    for i in range(r):
        for j in range(c):
            if a[i][j]=='?':
                ti = i
                tj = i
                while ti>=0:
                    if a[ti][j]!='?':
                        ans[i][j] = a[ti][j]
                        break
                    ti-=1
                if ans[i][j]=='?':
                    while tj<r:
                        if a[tj][j]!='?':
                            ans[i][j] = a[tj][j]
                            break
                        tj+=1
    return ans
                                    
for t in xrange(input()):
    arr = []
    r,c = map(int,raw_input().strip().split())
    farr = [[None]*c for i in range(r)]
    cols = ["" for i in range(c)]
    for i in range(r):
        s = raw_input()
        arr.append(s)
        for j in range(c):
            cols[j]+=s[j]
    rows = '?'*c in arr
    colsf = '?'*r in cols
    #print cols
    arr = map(list,arr)
    if rows and not colsf:
        arr = colwise(arr,r,c)
    elif colsf and not rows:
        arr = rowwise(arr,r,c)
    else:
        #print "YES"
        while check(arr):
            arr = rowwise(arr,r,c)
            arr = colwise(arr,r,c)

    print "Case #{}:".format(t+1)
    for i in range(r):
        print "".join(arr[i])