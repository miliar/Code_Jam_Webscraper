#/usr/bin/env python2.7
#-*- coding:utf-8 -*-
#huanghaiping2@gmail.com

import sys

def readline():
    return sys.stdin.readline()

if __name__ == '__main__':
    T = int(readline())
    for i in xrange(T):
        ans1 = int(readline())
        rows1 = []
        for j in xrange(4):
            rows1.append(set(readline().strip().split(' ')))
        ans2 = int(readline())
        rows2 = []
        for j in xrange(4):
            rows2.append(set(readline().strip().split(' ')))
        interSet = rows1[ans1-1] & rows2[ans2-1]
        print "Case #%s:" % (i+1),
        interSetLen = len(interSet)
        if 1 == interSetLen:
            print interSet.pop()
        elif 0 == interSetLen:
            print "Volunteer cheated!"
        else:
            print "Bad magician!"

