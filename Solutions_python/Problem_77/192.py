import sys

from itertools import permutations

def ncorrect(lst):
    correct = 0
    for i in range(len(lst)):
        if lst[i] == i+1:
            correct += 1
    return correct

def fact(n):
    return reduce(lambda x,y: x*y, range(1,n+1))

def counts(n): 
    counts = {}
    for p in permutations(range(1,n+1)):
        counts[ncorrect(p)] = counts.get(ncorrect(p), 0) + 1
    return counts

def hits(n):
    if n == 1:
        return 0
    c = counts(n)
    del c[n]
    zero = c[0]
    del c[0]
    f = fact(n)
    g = (1-float(zero)/fact(n))*(1.0/(fact(n)-zero) + sum(hits(n-k)*(float(v)/(fact(n)-zero)) for k,v in c.items()))
    r = 1./(1-float(zero)/fact(n))
    return (1+g)*r - 1

def cycle_lengths(lst):
    starts = set(lst)
    cycle_sum = 0.0
    while starts:
        cycle_len = 1
        start = list(starts)[0]
        starts.remove(start)
        cur = lst[start-1]
        while cur != start:
            starts.remove(cur)
            cycle_len += 1
            cur = lst[cur-1]
        cycle_sum += cycle_len if cycle_len != 1 else 0
    return cycle_sum

def solve_test(test):
    lst = map(int, test)
    return '%.6f' % (cycle_lengths(lst))

sequence = sys.stdin.readlines()
    
numtests = int(sequence[0])
for i in range(numtests):
    print 'Case #%d: %s' % (i+1,solve_test(sequence[2*i+2].split()))
