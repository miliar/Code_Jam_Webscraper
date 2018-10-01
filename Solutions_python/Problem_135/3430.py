# coding: utf-8 
from __future__ import division
import itertools
import math
#import numpy

def read_word(f):
	return next(f).strip()

def read_int(f, b=10):
	return int(read_word(f), b)

def read_letters(f):
	return list(read_word(f))

def read_digits(f, b=10):
	return [int(x, b) for x in read_letters(f)]

def read_words(f, d=' '):
	return read_word(f).split(d)

def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]
 
def read_arr(f, R, reader=read_ints, *args, **kwargs):
    res = []
    for i in range(R):
        res.append(reader(f, *args, **kwargs))
    return res
 
def solve(solver, fn, out_fn=None):
    in_fn = fn + '.in'
    if out_fn is None:
        out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            T = read_int(fi)
            for i in range(T):
                case = read_case(fi)
                res = solver(case)
                write_case(fo, i+1, res)
 
################################################################################
 
def read_case(f):
    A1 = read_int(f)
    D1 = 4*['0']
    #print int('12', 10)
    for i in range(0, 4):
      (C1, C2, C3, C4) = read_ints(f)
      print (C1, C2, C3, C4, i)
      D1[i] = (C1, C2, C3, C4)
    A2 = read_int(f)
    D2 = 4*['0']
    for i in range(0, 4):
      (C1, C2, C3, C4) = read_ints(f)
      D2[i] = (C1, C2, C3, C4)
    return (A1, D1, A2, D2)
 
def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')
 
################################################################################

INF = float('inf')
 
import heapq

def check_pal(N):
    Ds = [int(x, 10) for x in list(str(N))]
    #print Ds
    res = True
    for i in range(len(Ds)):
        if (i >= math.ceil(len(Ds)/2)):
            return res

        if Ds[i] != Ds[len(Ds)-1-i]:
            res = False

    return res

    

 
def solve_small(case):
    (A1, D1, A2, D2) = case
    print (A1, D1, A2, D2)
    AD = 16*['0']

    for K in D1[A1-1]:
        AD[K-1] = '1'
    print AD
    
    cnt = 0
    res = 0
    for K in D2[A2-1]:
        if(AD[K-1] == '1'):
            res = K    
        cnt += int(AD[K-1])
    #Ks = D2[A2-1]
    #for K in Ks:

    if cnt == 0:
        return 'Volunteer cheated!'
    elif cnt == 1:
        return res
    else:
        return 'Bad magician!'

    #sqrtA = int(math.ceil((math.sqrt(A))))
    #sqrtB = int(math.floor((math.sqrt(B))))

    #print (sqrtA, sqrtB)

    #for i in range(sqrtA, sqrtB + 1):
    #    N = i**2
    #    if check_pal(i) is True and check_pal(N) is True:
    #        print (i, N)
    #        res = res + 1






    return res

#solve_large = solve_small

def solve_large(case):
    (A, B) = case
    print (A, B)
    res = 0
    sqrtA = int(math.ceil((math.sqrt(A))))
    sqrtB = int(math.floor((math.sqrt(B))))

    sqrtAs = [int(x, 10) for x in list(str(sqrtA))]
    sqrtBs = [int(x, 10) for x in list(str(sqrtB))]

    #print sqrtAs

    res = 0
    #print (len(sqrtAs), len(sqrtBs))
    for length in range(len(sqrtAs), len(sqrtBs) + 1):
        #print "cur length: " + str(length)
        if length%2 == 0:
            lowhalf = int(length/2)*['0']
            lowhalf[0] = '1'
            highhalf = int(length/2)*['9']
            low = int("".join(lowhalf))
            high = int("".join(highhalf))
            #val = low
            for val in range(low, high+1):
            #while val < high+1:
                strhalf = [str(int(x, 10)) for x in list(str(val))]
                #print (strhalf, strhalf[::-1])
                N = "".join(strhalf) + "".join(strhalf[::-1])
                N = int(N)
                #print N
                #val +=1

                if N < sqrtA:
                    continue
                elif N > sqrtB:
                    break
                else:
                    if check_pal(N**2) is True:
                        res = res + 1
                
                

        else:
            lowhalf = int((length+1)/2)*['0']
            lowhalf[0] = '1'
            highhalf = int((length+1)/2)*['9']
            strlen = len(lowhalf)
            low = int("".join(lowhalf))
            high = int("".join(highhalf))
            #val = low
            for val in range(low, high+1):
            #while val < high+1:
                strhalf = [str(int(x, 10)) for x in list(str(val))]
                #print strhalf
                #print strlen
                if strlen == 1:
                    N = "".join(strhalf)
                else:
                    N = "".join(strhalf[0:strlen-1]) + "".join(strhalf[::-1])
                N = int(N)
                #print N

                #val+=1

                if N < sqrtA:
                    continue
                elif N > sqrtB:
                    break
                else:
                    if check_pal(N**2) is True:
                        res = res + 1


    return res




solve(solve_small, "MagicTrick")
#solve(solve_large, "FairnSquare")
