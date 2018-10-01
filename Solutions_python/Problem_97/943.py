'''
Solution to Problem 3 in GCI 2012's Qualifiction Round.

(C) 2012 Aviral Dasgupta.
www.aviraldg.com
'''

def gen_pair(n, m):
    i_m, i_n = m, n
    (n, m) = map(str, (n, m))
    for i in xrange(1, len(n)):
        n1 = n[i:] + n[:i]
        i_n1 = int(n1)
        if i_n < i_n1 <= i_m:
            yield (n, n1)

def count_solutions(a, b):
    k = set()
    for n in xrange(a, b+1):
        for i in gen_pair(n, b):
            k.add(i)
    return len(k)

def main():
    N = int(raw_input())
    for i in xrange(N):
        A, B = map(int, raw_input().split(' '))
        print 'Case #{0}: {1}'.format(i+1, count_solutions(A, B))

if __name__ == '__main__':
    main()
