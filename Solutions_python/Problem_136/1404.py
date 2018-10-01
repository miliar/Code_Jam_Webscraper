#!/usr/bin/env python

def cookie_time(c,f,x):
    time = 0.0
    cs_sec = 2.0
    while x/cs_sec > c/cs_sec + x/(cs_sec+f):
        time += c/cs_sec
        cs_sec += f
    return time + x/cs_sec

def main():
    t = int(raw_input())
    for tc in range(1,t+1):
        [c, f, x] = map(float,raw_input().split())
        res = cookie_time(c,f,x)
        print "Case #%d: %.7f" % (tc, res)


if __name__ == '__main__':
    main()