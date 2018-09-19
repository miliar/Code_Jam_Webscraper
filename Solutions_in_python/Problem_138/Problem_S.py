import math
from array import array


f = open('D-large.in', 'r')
g = open('Output.txt', 'w')
T = [int(s) for s in f.readline().split() if s.isdigit()][0]


for i in range (0,T):

    actual_line = [int(s) for s in f.readline().split()]
    N = actual_line[0]
   

    naomi = array('d',sorted([float(s) for s in f.readline().split()]))
    ken   = array('d',sorted([float(s) for s in f.readline().split()]))


    score1 = 0
    n_w_n = 0
    k_w_n = 0
    k_b_n = N-1
    n_b_n = N-1

    for k in range(0,N):
       
        n_w = naomi[n_w_n]
        n_b = naomi[n_b_n]
        k_w = ken[k_w_n]
        k_b = ken[k_b_n]

        if (n_w > k_b):
            score1 += N - n_w_n 
            break
        elif (k_w > n_b):
            break
        elif (n_w < k_w):
            n_w_n += 1
            k_b_n -= 1
        else:
            n_w_n += 1
            k_w_n += 1
            score1  += 1


    score2 = 0
    n_w_n = 0
    k_w_n = 0
    k_b_n = N-1
    n_b_n = N-1

    for k in range(0,N):
       
        n_w = naomi[n_w_n]
        n_b = naomi[n_b_n]
        k_w = ken[k_w_n]
        k_b = ken[k_b_n]

        if (n_w > k_b):
            score2 += (n_b_n + 1) - n_w_n 
            break
        elif (k_w > n_b):
            break
        elif (n_b > k_b):
            n_b_n -= 1
            k_w_n += 1
            score2 += 1
        else:
            n_b_n -= 1
            k_b_n -= 1
     
    ans_str = 'Case #'+str(i+1)+': '+str(score1)+' '+str(score2)
    g.write(ans_str)
    if (i+1 != T):
        g.write('\n')

g.close()
