import collections
import sys
import random
t=int(input())
f=open('/home/shubham/python_scripts/R1Q1short.txt',"w")
for q in range(t):
    r,c = [int(i) for i in input().split(' ')]
    l=[]
    for i in range(r):
        l.append(list(input()))
    for i in range(len(l)):
        if(l[i].count('?')!=c):
            f=0
            x=''
            for j in range(len(l[i])):
                if(l[i][j]!='?'):
                    x=l[i][j]
                    if(f==0):
                        for k in range(0,j):
                            l[i][k]=x
                        f=1
                else:
                    if(x!=''):
                        l[i][j]=x
        else:
            if(i==0):
                pass
            else:
                if(l[i-1]!='?'):
                    l[i]=l[i-1]
    for i in range (len(l)):
        if(l[i][0]!='?'):
            f=1
            p=i
            break
    for i in range(0,p):
        l[i]=l[p]
    print("Case #%d:"%(q+1))
    for i in l:
        for j in i:
            print(j, end='')
        print()