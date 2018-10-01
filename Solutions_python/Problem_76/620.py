#! /usr/bin/python

import sys, os, math

f = file(sys.argv[1])
lines = f.readlines()
f.close()

inputData = []
cases = int(lines[0].strip())

pos = 1
for c in range(cases):
    inputData.append([int(cv) for cv in lines[pos+1].strip().split()])
    #print(lines[pos].strip())
    #print('seq, combinations, opposingElements')
    #print(seq, combinations, opposingElements)
    pos = pos + 2

def patrikAdd(no1, no2):
    if max(no1,no2) < 1:
        return 0
    base2_ind = int(math.log(max(no1,no2),2))+1
    result = 0
    for exp in range(base2_ind +1, -1, -1):
        d = 2 ** exp
        digit = 0
        if no1 >= d:
            no1 = no1 - d
            digit = digit +1
        if no2 >= d:
            no2 = no2 - d
            digit = digit +1
        result = result + (digit % 2)*d
    return result
def patrikSum(N):
    res = 0
    for nv in N:
        res = patrikAdd(res,nv)
    return res

print('patrick add test : 5+4 = %s (should equal 1) ' % patrikAdd(5,4))
print('patrick add test : 7+9 = %s (should equal 14) ' % patrikAdd(7,9))
print('patrick add test : 50+10 = %s (should equal 56) ' % patrikAdd(50,10))
print('*testing if order matters for patrick add (p+) *')
print('5 (p+) 45 (p+) 17 = %i' % patrikAdd(patrikAdd(5, 45),17))
print('5 (p+) 17 (p+) 45 = %i' % patrikAdd(patrikAdd(5, 17),45))
print('45 (p+) 17 (p+) 5 = %i' % patrikSum([45,17,5]))

def analyse(candies):
    global best_found_sean
    best_found_sean = -1
    def walkCombinations(pile, sean, patrik):
        if len(pile) > 0:
            #option 1, candy goes to sean
            walkCombinations(pile[1:], sean[:] + pile[0:1], patrik[:])
            #option 2, candy goes to patrik
            walkCombinations(pile[1:], sean[:], patrik[:] + pile[0:1])
        else:
            global best_found_sean
            if len(sean) > 0 and len(patrik) > 0:
                if patrikSum(sean) == patrikSum(patrik):
                    if sum(sean) > best_found_sean:
                        best_found_sean = sum(sean)
    walkCombinations(candies, [] , [])
    if best_found_sean > -1:
        return best_found_sean
    else:
        return 'NO'

output = []
for case,input in enumerate(inputData):
    print('case %i : inputs %s' % (case+1, input))
    res = analyse(input)
    output.append('Case #%i: %s' % (case+1, res))
    print(output[-1])

f = file(sys.argv[1].replace('.in','.out'),'w')
f.write('\n'.join(output))
f.close()
