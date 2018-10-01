#!/usr/bin/env python

def main():
    T = int(raw_input())
    for t in xrange(1, T+1):
        n, shy = raw_input().split()
        people = int(shy[0])
        cont = 0
        for pos in xrange(1, len(shy)): 
            num = int(shy[pos])
            dif = 0
            if people < pos:
                dif = pos - people
                cont += dif
            people += num + dif

        print 'Case #%d: %d' % (t, cont)

if __name__ == "__main__":
    main()

