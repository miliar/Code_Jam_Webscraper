'''
Problem
@YEAR Google Code Jam 2011: Qualification Round
@ID C
@NAME Candy Splitting
@URL http://code.google.com/

Solution
@AUTHOR Wonjohn Choi (http://capcs.wordpress.com/)
@LANG Python 3
@ETC Brute-Force (expect to solve only small input)
@RESULT
'''
from itertools import product

def divide(bag):
    for choices in product([0, 1], repeat=len(bag)):
        if list(choices)!=[0]*len(bag) and list(choices)!=[1]*len(bag):
            yield [[bag[i] for i in range(len(bag)) if choices[i]==0], [bag[i] for i in range(len(bag)) if choices[i]==1]]

def xorSum(bag):
    if len(bag)==0: return 0
    
    sum = bag[0]
    for i in range(1, len(bag)):
        sum^=bag[i]
    return sum

def solve():
    t = int(input())
    for i in range(t):
        n = int(input())
        bag = list(map(int, str(input()).strip().split(' ')))
        
        maxS = -1
        for s, p in divide(bag): #s->Sean p->Patrick 
            if xorSum(s)==xorSum(p):
                newS = sum(s)
                if newS>maxS:
                    maxS = newS
        
        print('Case #%d: '%(i+1), end='')
        if maxS==-1:
            print('NO')
        else:
            print(maxS)
solve()