from math import *
from sys import stdout

def get_ints():
    l = map(int,raw_input().split())
    return l

def get_floats():
    l = map(float,raw_input().split())
    return l
        
    
def func():
    T=int(raw_input())
    for cases in range(1,T+1):
        l = get_ints()
        a,b,k = l[0],l[1],l[2]
        
        ans = []
        
        for i in range(0,a):
            for j in range(0,b):
                z = i & j
                if z < k and z >=0:
                    ans.append(z)
        #print ans
        print "Case #{0}: {1}".format(cases,len(ans))

func()
