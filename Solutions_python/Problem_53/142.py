import os
import sys

n = int( sys.stdin.readline().strip() )

for i in range( n ):
    a, num = sys.stdin.readline().strip().split(' ')
    a = int(a)
    num = int(num)
    num = num & ( 2**a - 1 )
    res = True
    for z in range( a ):
        if not ( num & 1 == 1 ):
            res = False
            break
        num = num >> 1
    print 'Case #%d: %s' % ( i+1, res and "ON" or "OFF", )
