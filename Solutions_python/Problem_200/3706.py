#!/usr/bin/python
# coding: utf-8

t=int(raw_input())
for i in xrange(t):
    n=long(raw_input())
    j=n
    while(j>=0):
        num=str(j)
        length=len(num)
        cnt=-1
        for k in xrange(length-1):
            if(num[k]>num[k+1]):
                cnt=k+1
                break
        if(cnt==-1):
            print "Case #"+str(i+1)+": "+str(j)
            break
        else:
            s=''
            for k in xrange(cnt):
                s+=num[k]
            for k in xrange(cnt,length):
                s+='0'
            j=long(s)
        j-=1
