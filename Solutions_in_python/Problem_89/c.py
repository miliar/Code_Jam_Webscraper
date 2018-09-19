import sys
filein, fileout = sys.argv[1:3]

from math import log,floor
primes_list = [2]

def primes():
    for p in primes_list:
        yield p
    k = p+1
    while True:
        isprime = True
        for p in primes_list:
            if k % p == 0:
                isprime = False
                break
        if isprime:
            primes_list.append(k)
            yield k
        k += 1

def solve(n):
    if n == 1: return 0
    powers = []
    for p in primes():
        if p <= n:
            powers.append(floor(log(n,p)))
        else:
            break
    return sum(powers)-len(powers)+1

if __name__ == '__main__':
    with open(filein, 'rU') as f1, open(fileout, 'w') as f2:
        T = int(f1.readline())
        for case in range(T):
            n = int(f1.readline())
            f2.write("Case #{}: {}\n".format(case+1, solve(n)))

