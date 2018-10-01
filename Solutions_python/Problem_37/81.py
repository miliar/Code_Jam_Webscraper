import sys
import itertools as it

def nats():
    n=0
    while True:
        n += 1
        yield n

def base_expand(n,b):
    exp = list()
    while n>0:
        d = n%b
        exp.insert(0, d)
        n/=b
    return exp

def happy_work(n, b):
    seen = []
    while True:
        print n, b
        if n==1:
            return True
        elif n in seen:
            return False
        else:
            seen.append(n)
            n = sum([x*x for x in base_expand(n,b)])

happy_m = dict()
def happy(*a):
    if not happy_m.has_key(a):
        happy_m[a] = happy_work(*a)
    return happy_m[a]

def min_happy(bases):
    ns = nats()
    ns.next()
    for n in ns:
        if all([happy(n,b) for b in bases]):
            return n

def input_ints():
    return [int(x) for x in sys.stdin.readline().strip().split()]

if __name__ == "__main__":
    (T,) = input_line((int,))
    for case in range(1, T+1):
        bases = input_ints()

        print "Case #%d: %d" % (case, min_happy(bases))
