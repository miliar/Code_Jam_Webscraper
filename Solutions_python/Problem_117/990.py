#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tim
#
# Created:     13/04/2013
# Copyright:   (c) tim 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tim
#
# Created:     13/04/2013
# Copyright:   (c) tim 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def check (arr):
    for i in range(0, N):
        for j in range( 0, M):
            if arr[i][j] < min ( (arr[0][j], arr[N-1][j], arr[i][0], arr[i][M-1] ) ):
               return 'NO'
    return 'YES'

def main():
    pass

if __name__ == '__main__':
    main()

result = []
T = 0

with open('B-large.IN') as f:
    T = int(f.readline())

    for t in range(0, T):
        arr = f.readline().split(' ')
        N = int(arr[0])
        M = int(arr[1])
        arr = []
        iarr = []
        for n in range(0, N):
            arr.append ([int (e) for e in  f.readline().split(' ') ] )
            iarr.append( [100 for e in range(0, M)])
        ##
        for i in range(0,N) :
            ma = max( arr[i] )
            for j in range(0, M):
                if iarr[i][j] > ma:
                    iarr[i][j] = ma
        ##
        for j in range(0,M) :
            ma = max( [arr[i][j] for i in range(0, N) ] )
            for i in range(0, N):
                if iarr[i][j] > ma:
                    iarr[i][j] = ma
        ### check equel
        rs = 'YES'
        for i in range(0,N):
            for j in range( 0, M):
                if arr[i][j] != iarr[i][j]:
                    rs =  'NO'
                    break;
            if rs == 'NO':
                break;
        result.append( rs )

###############
with open('B-large.OUT', 'w') as f:
    for  i in range(0, T):
        f.write("Case #%d: %s\n" % (i+1, result[i]) )