def readint():
    return int(input())


def readfloat():
    return float(input())


def readarray(N, foo=input):
    return [foo() for i in range(N)]


def readlinearray(foo=int):
    return list(map(foo, input().split()))


def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


def gen_primes(max):
    primes = [1] * (max + 1)
    for i in range(2, max + 1):
        if primes[i]:
            for j in range(i + i, max + 1, i):
                primes[j] = 0
    primes[0] = 0
    return [x for x in range(2, max + 1) if primes[x]]


case_number = readint()
for case in range(case_number):
    S = input()
    if S[0] == '1' and S < '1' * len(S):
        a = '9' * (len(S) - 1)
    else:
        a = ''
        for c in S:
            for d in range(1, 10):
                if a + str(d) * (len(S) - len(a)) > S:
                    a += str(d - 1)
                    break
            else:
                a += '9' * (len(S) - len(a))
                break
    print("Case #%d: %s" % (case + 1, a))
