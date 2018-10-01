#!/usr/bin/python

import sys
import math

def factorial( n ):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def nchoosek( n, k ):
    #return factorial(n)/(factorial(k)*factorial(n-k))
    answer = 1
    for i in range(1,k+1):
        answer *= (n - (k - i))
        answer /= i
    return answer


def reduce_answer( N, K ):
    #print K
    if K < 1:
        print "Problem!!!"
        return([-1,-1])
    if K == 1:
        if N%2 == 1:
            return [(N-1)/2,(N-1)/2]
        else:
            return [N/2,(N-2)/2]
    elif K%2 == 1 and N%2 == 1:
        return reduce_answer((N-1)/2, (K-1)/2)
    elif K%2 == 1 and N%2 == 0:
        return reduce_answer((N-2)/2, (K-1)/2)
    elif K%2 == 0 and N%2 == 1:
        return reduce_answer((N-1)/2, K/2)
    elif K%2 == 0 and N%2 == 0:
        return reduce_answer(N/2, K/2)




f = open( sys.argv[1] )

num_cases = int(f.readline().split()[0])

for case_num in range(num_cases):
    line = f.readline().strip()
    if len(line) <= 0:
        continue
    [N, K] = line.split()
    [N, K] = [int(N), int(K)]


    [max_dist, min_dist] = [int(x) for x in reduce_answer(N, K)]

    print "Case #" + str(case_num+1) + ":",max_dist, min_dist 

