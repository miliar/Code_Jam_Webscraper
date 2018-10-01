#!/usr/bin/python

# By Jesse -- jesse.wanderer@gmail.com

def main():
    n = int(raw_input())
    x = map(int, raw_input().split())
    y = map(int, raw_input().split())
    x.sort()
    y.sort(reverse=True)
    print sum([x[i]*y[i] for i in range(n) ])

for i in range(int(raw_input())):
    print "Case #%d:" % (i+1),
    main()
