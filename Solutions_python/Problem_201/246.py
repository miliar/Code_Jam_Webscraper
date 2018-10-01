#!/usr/bin/python
import math
pw2 = [1 , 2 , 4 , 8 , 16 , 32 , 64 , 128 , 256 , 512 , 1024 , 2048 , 4096 , 8192 , 16384 , 32768 , 65536 , 131072 , 262144 , 524288 , 1048576 , 2097152 , 4194304 , 8388608 , 16777216 , 33554432 , 67108864 , 134217728 , 268435456 , 536870912 , 1073741824 , 2147483648 , 4294967296 , 8589934592 , 17179869184 , 34359738368 , 68719476736 , 137438953472 , 274877906944 , 549755813888 , 1099511627776 , 2199023255552 , 4398046511104 , 8796093022208 , 17592186044416 , 35184372088832 , 70368744177664 , 140737488355328 , 281474976710656 , 562949953421312 , 1125899906842624 , 2251799813685248 , 4503599627370496 , 9007199254740992 , 18014398509481984 , 36028797018963968 , 72057594037927936 , 144115188075855872 , 288230376151711744 , 576460752303423488 , 1152921504606846976]
def find_level(K):
    i = 0
    while i!= len(pw2):
        if pw2[i] > K:
            return i, K - pw2[i-1]
        i+=1
    print "ERROR"
    sys.exit(1)
def find_ans(N, K):
    l, offset = find_level(K)
    #print "Level-", l, "; Offset-", offset
    ans = N
    lt = [ ((N,), 1) ]
    for i in range(l):
        nlt = []
        for k in lt:
            cnt = k[1]
            tp = k[0]
            for j in tp:
                if j % 2 == 0:
                    nlt.append( ((j/2 - 1, j/2), cnt))
                else:
                    nlt.append( ( (j/2, j/2), cnt ))
        nlt = sorted(nlt, reverse = True)
        ind = 0
        lt = []
        while ind != len(nlt) :
            cnt = nlt[ind][1]
            val = nlt[ind][0]
            while ind != len(nlt) -1 and nlt[ind][0] == nlt[ind+1][0]:
                cnt += nlt[ind+1][1]
                ind += 1
            lt.append((val, cnt))
            ind += 1
    #print lt
    if offset < lt[0][1]:
        return lt[0][0]
    return lt[1][0]

T = int(raw_input())
for i in range(T+1)[1:]:
    ans = 0
    l = raw_input()
    N, K = l.split()
    N, K = int(N), int(K)
    ans1, ans2 = find_ans(N, K)
    print "Case #"+str(i)+": "+str(ans2) + " " +str(ans1)
