#!/usr/bin/python

import sys

line = sys.stdin.readline

ncases = int(line())

mem = {}

def primes(limit):  
    
    numbers = []  
    primes = []  
    
    if mem.keys().count(limit)>0:
        return mem[limit]

    for i in range(2, limit+1):  
        numbers.append(i)  
        
    while True:  
        if len(numbers) == 0:  
            break  
   
        prime = numbers[0] 
        if float(limit)/prime == limit/prime: 
            primes.append(prime)  
        multiples = []  
   
        for n in numbers:  
            if n % prime == 0:  
                multiples.append(n)  
                
        for n in multiples:  
            numbers.remove(n)  
   
    mem[limit] = primes

    return primes  

for i in range(0,ncases):
    [a, b, p] = map(int, line().split(" "))

    facts = []
    xed = []
    sum = 0

    for x in range (a,b+1):
        if xed.count(x)==0:
            if x >= p:
                for pr in primes(x):
                    if pr>=p:
                        facts.append(pr)

            for f in facts:
                curr = f
                mult = 1
                join = False
                while curr < a:
                    mult += 1
                    curr = f*mult
                while curr <= b:
                    xed.append(curr)
                    for pr in primes(curr):
                        if pr >= p and facts.count(pr) == 0:
                            facts.append(pr)
                    mult += 1
                    curr = f*mult

            sum += 1


    sys.stdout.write("Case #")
    sys.stdout.write(str(i+1))
    print ":",sum
