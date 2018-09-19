#!/usr/bin/python2.5
def main():
  for case in range(input()):
    n, k = map(int,raw_input().split())
    x = 2**n
    if k == 0:
        yes = False
    else:
        if k+1 & x-1 == 0:
            yes = True
        else:
            yes = False
    if yes:
        b = "ON"
    else:
        b = "OFF"
    print 'Case #%s: %s' % (case + 1, b )
main()