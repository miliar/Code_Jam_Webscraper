f = open('C-small-attempt1.in')
of = open('C-small-attempt1.out', 'w')

import itertools

def xor(x, y):
    return x^y

T = int(f.readline())
for i in range(T):

    N = int(f.readline())
    sean = 0

    candies = [int(x) for x in f.readline().split(' ')]

    for j in candies:
        rest = candies[:]
        rest.remove(j)
        if j == reduce(xor, rest):
            mval = max(j, sum(rest))
            if sean < mval:
                sean = mval
                
    for j in range(2,N):
        combinations = itertools.combinations(candies,j)
        for comb in combinations:
            rest = candies[:]
            for entry in comb:
                rest.remove(entry)
            if reduce(xor, comb) == reduce(xor, rest):
                mval = max([sum(rest), sum(comb)])
                if sean < mval:
                    sean = mval
                    

    if sean == 0:
        sean = 'NO'

    of.write("Case #{0}: {1}\n".format(i+1, sean))
    print i+1

f.close()
of.close()

print 'done'
