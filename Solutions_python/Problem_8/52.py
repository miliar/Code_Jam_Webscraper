import sys

def primes(n):
    """Generate a list of the prime numbers [2, 3, ... m] where
    m is the largest prime <= n."""
    n = n + 1
    sieve = range(n)
    sieve[:2] = [0, 0]
    for i in xrange(2, int(n**0.5)+1):
        if sieve[i]:
            for j in xrange(i**2, n, i):
                sieve[j] = 0
    # Filter out the composites, which have been replaced by 0's
    return [p for p in sieve if p]

def find_diff(a,b,p):
    interval = [[n] for n in range(a, b+1)]
    prime_numbers = [n for n in primes(b) if n>=p]
    for pn in prime_numbers:
        new_set = []
        to_be_removed = []
        for i in xrange(len(interval)):
            factor_of_pns = [n for n in interval[i] if n % pn == 0]
            if factor_of_pns:
                new_set.extend(interval[i])
                to_be_removed.append(i)
        if new_set:
            interval.append(new_set)
        z=0
        for x in to_be_removed:
            interval.pop(x-z)
            z+=1
    return len(interval)

def main ():
    cases = int(sys.stdin.readline())
    for x in xrange(cases):
        a, b, p = [int(k) for k in sys.stdin.readline().split()]
        print "Case #%s: %s" % (x+1, find_diff(a,b,p))
    return 0

if __name__ == "__main__":
    status = main()
    sys.exit(status)
