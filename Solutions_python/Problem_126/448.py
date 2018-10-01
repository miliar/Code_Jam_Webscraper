#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tim
#
# Created:     12/05/2013
# Copyright:   (c) tim 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
result = []
with open('A-small-attempt0.IN') as f:
    T = int(f.readline())

    for i in range(0, T):
        arr = f.readline().strip().split(' ')
        str = arr[0]
        N = int(arr[1])
        arr = []
        doans= []
        for c in str:
            if c == 'a' or c =='e' or c == 'i' or c== 'o' or c == 'u':
                arr.append(0)
            else:
                arr.append(1)
        #print arr, N
        sum = 0
        for i in range(0, len(arr)):
            if i < N:
                sum += arr[i]
            else:
                sum += arr[i]
                sum -= arr[i-N]
            if i >= N-1 and sum == N:
                doans.append(i-N + 1)
        #
        #print doans;
        cnt = 0;
        for i in range(0, len(arr) - N + 1):
            for j in range (i+N-1, len(arr)):
                for doan in doans:
                    if i <= doan and doan+N-1 <= j:
                        cnt += 1
                        break;
        result.append(int(cnt))
    ########################33

#print result
with open('A-small-attempt0.OUT', 'w') as f:
    for  i in range(0, T):
        f.write("Case #%d: %s\n" % (i+1, result[i]) )
