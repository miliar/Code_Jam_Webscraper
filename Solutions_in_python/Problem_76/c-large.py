import math
import operator
import functools

prob = "c"
size = "large"

f = open('{0}-{1}.in'.format(prob, size))
o = open('{0}-{1}.out'.format(prob, size), 'w+')
n = int(f.readline());

for i in range(n):
    c = int(f.readline())
    
    cs = f.readline().split(' ')
    candies = []
    for v in cs:
        candies.append(int(v))
    candies.sort()
    
    max_attempts = c
    attempt = 1
    
    match = False
    for j in range(max_attempts - 1):
        sean = candies[attempt:max_attempts + 1]
        pat = candies[-max_attempts:attempt]
        attempt = attempt + 1
        
        pat_xor = functools.reduce(operator.xor, pat)
        sean_xor = functools.reduce(operator.xor, sean)
        
        if pat_xor == sean_xor:
            match = True
            o.write('Case #{0}: {1}\n'.format(i+1, sum(sean)))
            break
    if ( match == False ):
        o.write('Case #{0}: NO\n'.format(i+1))