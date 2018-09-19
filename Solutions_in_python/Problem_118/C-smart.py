#!/usr/bin/env python3

def is_palindrome(n):
    if(n == 0): return False

    s = str(n)

    if(s == s[::-1]):
        return True
    return False

#def generate_even(length):
    #M = 1<<length
#
    #for i in range(M):
        #count = 0
        #conv = 0
        #rconv = 0
        #for l in range(length):
            #if(i & (1<<l) != 0):
                #count += 1
                #conv += 10**l
                #rconv += 10**(length-l-1)
#
        #if(count > 3): continue
#
        #result = conv*10**length + rconv
        #result *= 10
        #result += 1
        #result += 10**(length*2 + 1)
        #yield (result, count)
def formatted(number, length):
    nrev = int(str(number)[::-1])

    result = 1 + 10**(2*length+1)
    result += number * 10**(length+1)
    result += nrev * 10
    #print(result)
    return result

def generate_even(length):
    number = 0
    for i in range(length):
        number += 10**i
        for j in range(i+1, length):
            number += 10**j
            for k in range(j+1, length):
                yield (formatted(number + 10**k, length), 3)
            yield (formatted(number, length), 2)
            number -= 10**j
        yield (formatted(number, length), 1)
        number -= 10**i
    yield (formatted(number, length), 0)

def generate(length):
    for g, c in generate_even(length):
        yield g

        exp = 10**(length+1)
        lower = g % exp
        upper = (g // exp) * exp

        yield lower + upper*10
        yield lower + exp + upper*10
        if(c != 3): yield lower + 2*exp + upper*10

    #print("Suggesting", 2*(10**(length*2)) + 2,
#2*(10**(length*2 + 1)) + 2,
#2*(10**(length*2)) + 2 + 2*(10**(length)))

    yield 2*(10**(length*2)) + 2
    yield 2*(10**(length*2 + 1)) + 2 
    yield 2*(10**(length*2)) + 2 + 1*(10**(length))

sqrts = [1,2,3]
for l in range(0, 51):
    for s in generate(l):
        if(not is_palindrome(s*s)): continue
        sqrts += [s]
        #print(s)
    #print("generated l = " +str(l))
#print("total count:", len(sqrts))

sqrts = sorted(sqrts)
#print(sqrts[-1])
#print(sqrts[-1]**2)

T = int(input())

for t in range(T):
    s = input().split()
    A = int(s[0])
    B = int(s[1])
    count = 0
    for q in sqrts:
        r = q**2
        #print("Considering q = " + str(q) + ", r = " + str(r))
        if(r < A): continue
        if(r > B): break
        if(r >= A and r <= B): count += 1
    print("Case #" + str(t+1) + ": " + str(count))
