import sys;
from math import sqrt


primes = [2,3,5,7,11,13,17,19,23,29,
          31,37,41,43,47,53,59,61,67,71,
          73,79,83,89,97,101,103,107,109,113,
          127,131,137,139,149,151,157,163,167,173,
          179,181,191,193,197,199,211,223,227,229,
          233,239,241,251,257,263,269,271,277,281,
          283,293,307,311,313,317,331,337,347,349,
          353,359,367,373,379,383,389,397,401,409,
          419,421,431,433,439,443,449,457,461,463,
          467,479,487,491,499,503,509,521,523,541,
          547,557,563,569,571,577,587,593,599,601,
          607,613,617,619,631,641,643,647,653,659,
          661,673,677,683,691,701,709,719,727,733,
          739,743,751,757,761,769,773,787,797,809,
          811,821,823,827,829,839,853,857,859,863,
          877,881,883,887,907,911,919,929,937,941,
          947,953,967,971,977,983,991,997]


class Problem:
    def __init__(self, tc):
        self.A = tc[0][0]
        self.B = tc[0][1]
        self.P = tc[1]

    def solve(self):
        for_test = [x for x in primes if x>=self.P and x<=self.B]
        z = ([set([x]) for x in range(self.A, self.B+1)])
        for i in for_test:
            z = self.check(z, i)

        return len(z)

    def check(self, a, i):
        z = [set([])]
        for s in a:
            if self.divides(s, i):
                z[0].update(s)
            else:
                z.append(s)
        if z[0]:
            return z
        else:
            return z[1:]


    def divides(self, a, n):
        for x in a:
            if x % n == 0:
                return True
        return False

def parse_input(f):
    n = int(f.readline())
    return (read_test_case(f) for i in range(n))

def read_test_case(f):
    tc = [int(x) for x in f.readline().split()]
    return ((tc[0], tc[1]), tc[2])


def print_result(i, r):
    print 'Case #%d: %d' % (i, r)



if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    input = parse_input(sys.stdin)
    n = 0
    for tc in input:
        p = Problem(tc)
        r = p.solve()
        n = n+1
        print_result(n, r)
