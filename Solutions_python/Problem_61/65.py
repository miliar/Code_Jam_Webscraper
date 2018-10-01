#! /usr/bin/env python
#coding=utf-8

l = [[-1 for i in range(505)] for i in range(505)]
r = [[-1 for i in range(505)] for i in range(505)]

def main():
    fh = open(raw_input())
    
    t = int(fh.readline())
    for p in range(t):
        
        k = int(fh.readline())
        s = 0
        for i in range(1, k, 1):
            s += calc(k, i)
        print "Case #%d: %d" % (p + 1, s % 100003)
    

def c(m, n):
    if r[m][n] != -1:
        return r[m][n]
    s = 1
    for i in range(m - n + 1, m + 1, 1):
        s *= i
    for i in range(n):
        s /= (i+1)
        
    r[m][n] = s
    return s
    

def calc(p, q):
    if q == 1:
        return 1
    if q == 2:
        return 1
    if q == p - 1:
        return 1
    if l[p][q] != -1:
        return l[p][q]
    
    sum = 0
    for i in range(1, q, 1):
        sum += calc(q, i) * c(p - q - 1, q - i - 1)
    
    l[p][q] = sum
    return sum

if __name__ == "__main__" :
    main()
