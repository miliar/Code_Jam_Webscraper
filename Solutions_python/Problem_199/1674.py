import resource, sys
# resource.setrlimit(resource.RLIMIT_STACK, 2**12)
sys.setrecursionlimit(10**6)

FILENAME = 'a-large.txt'

f = open(FILENAME)

def invert(c):
    if c == '+':
        return '-'
    return '+'

def answer(pancakes, k):
    if len(pancakes) < k:
        if '-' in pancakes:
            return 'IMPOSSIBLE'
        return 0
    if len(pancakes) == k:
        if '+' in pancakes and '-' in pancakes:
            return 'IMPOSSIBLE'
        if '-' in pancakes:
            return 1
        return 0

    if pancakes[0] == '+':
        return answer(pancakes[1:], k)
    else:
        new_pancakes = ''.join(invert(c) for c in pancakes[1:k]) + pancakes[k:]
        subval = answer(new_pancakes, k)
        if subval == 'IMPOSSIBLE':
            return subval
        else:
            return subval + 1


num_cases = int(f.readline())
for case in xrange(1, num_cases + 1):
    pancakes, k = f.readline().split()
    val = answer(pancakes, int(k))
    print 'Case #{}: {}'.format(case, val)
