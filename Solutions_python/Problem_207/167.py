import numpy as np
import math

#------------------------------------
# Read inputs
t = int(raw_input())
for i in xrange(1, t + 1):
    N, R, O, Y, G, B, V = [int(s) for s in raw_input().split(" ")]

    # print
    # print N, R, O, Y, G, B, V
    A = ['' for j in range(0,N)]

    if O+G+V==0:
        c = ['R','Y','B']
        m = [R,Y,B]
        if 2*max(m)>N:
            print "Case #{}: ".format(i) + "IMPOSSIBLE"
        else:
            i1 = m.index(max(m))
            idx = 0
            while idx<N:
                if m[i1]>0:
                    A[idx] = c[i1]
                    m[i1] -= 1
                    idx += 2
                else:
                    i1 = m.index(max(m))
            idx = 1
            while idx<N:
                while idx<N:
                    if m[i1]>0:
                        A[idx] = c[i1]
                        m[i1] -= 1
                        # assert(A[idx-1]!=c[i1] and A[(idx+1)%N]!=c[i1])
                        idx += 2
                    else:
                        i1 = m.index(max(m))
            # assert(max(m)==0)
            print "Case #{}: ".format(i) + ''.join(A)
    else:
        if O>B or G>R or V>Y:
            print "Case #{}: ".format(i) + "IMPOSSIBLE"
        else:
            if O==B and O>0:
                if O+B==N:
                    for j in range(N):
                        if j%2==0:
                            A[j] = 'O'
                        else:
                            A[j] = 'B'
                    print "Case #{}: ".format(i) + ''.join(A)
                elif O+B<N:
                    print "Case #{}: ".format(i) + "IMPOSSIBLE"
            elif G==R and G>0:
                if G+R==N:
                    for j in range(N):
                        if j%2==0:
                            A[j] = 'G'
                        else:
                            A[j] = 'R'
                    print "Case #{}: ".format(i) + ''.join(A)
                elif G+R<N:
                    print "Case #{}: ".format(i) + "IMPOSSIBLE"
            elif V==Y and V>0:
                if V+Y==N:
                    for j in range(N):
                        if j%2==0:
                            A[j] = 'V'
                        else:
                            A[j] = 'Y'
                    print "Case #{}: ".format(i) + ''.join(A)
                elif V+Y<N:
                    print "Case #{}: ".format(i) + "IMPOSSIBLE"
            else:
                c1 = ['R','Y','B']
                m1 = [R,Y,B]

                c2 = ['','','']
                m2 = [0,0,0]
                if G>0:
                    m1[0] -= (G+1)
                    t1 = ''
                    for j in range(2*G+1):
                        if j%2==0:
                            t1 += 'R'
                        else:
                            t1 += 'G'
                    c2[0] = t1
                    m2[0] = 1
                if V>0:
                    m1[1] -= (V+1)
                    t1 = ''
                    for j in range(2*V+1):
                        if j%2==0:
                            t1 += 'Y'
                        else:
                            t1 += 'V'
                    c2[1] = t1
                    m2[1] = 1
                if O>0:
                    m1[2] -= (O+1)
                    t1 = ''
                    for j in range(2*O+1):
                        if j%2==0:
                            t1 += 'B'
                        else:
                            t1 += 'O'
                    c2[2] = t1
                    m2[2] = 1

                m3 = list(np.array(m1) +np.array(m2))
                N = sum(m1)+sum(m2)
                # print c1,m1,c2,m2,m3,N

                if 2*max(m3)>N:
                    print "Case #{}: ".format(i) + "IMPOSSIBLE"
                else:
                    i1 = m3.index(max(m3))
                    idx = 0
                    while idx<N:
                        if m1[i1]>0:
                            A[idx] = c1[i1]
                            m1[i1] -= 1
                            idx += 2
                        elif m2[i1]>0:
                            A[idx] = c2[i1]
                            m2[i1] -= 1
                            idx += 2
                        else:
                            m3 = list(np.array(m1) +np.array(m2))
                            i1 = m3.index(max(m3))
                    idx = 1
                    while idx<N:
                        while idx<N:
                            if m1[i1]>0:
                                A[idx] = c1[i1]
                                m1[i1] -= 1
                                # assert(A[idx-1]!=c[i1] and A[(idx+1)%N]!=c[i1])
                                idx += 2
                            elif m2[i1]>0:
                                A[idx] = c2[i1]
                                m2[i1] -= 1
                                # assert(A[idx-1]!=c[i1] and A[(idx+1)%N]!=c[i1])
                                idx += 2
                            else:
                                m3 = list(np.array(m1) +np.array(m2))
                                i1 = m3.index(max(m3))
                    # assert(max(m)==0)
                    print "Case #{}: ".format(i) + ''.join(A)
    # print "Case #{}:".format(i) ,
