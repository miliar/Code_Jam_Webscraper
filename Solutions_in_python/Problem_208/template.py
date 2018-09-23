from re import *
from sys import stderr
def readint():
    return int(input())
def readfloat():
    return float(input())
def readarray(N, foo=input):
    return [foo() for i in range(N)]
def readlinearray(foo=int):
    return list(map(foo, input().split()))

def NOD(a, b):
    while b:
        a,b = b, a%b
    return a

def gen_primes(max):
    primes = [1]*(max+1)
    for i in range(2, max+1):
        if primes[i]:
            for j in range(i+i, max+1, i):
                primes[j] = 0
    primes[0] = 0
    return [x for x in range(max+1) if primes[x]]

def is_prime(N):
    i = 3
    if not(N % 2):
        return 0
    while i*i < N:
        if not(N % i):
            return 0
        i += 3
    return 1

case_number = readint()
for case in range(case_number):
    N, Q = readlinearray()
    horses = readarray(N, readlinearray)
    distances = readarray(N, readlinearray)
    points = readarray(Q, readlinearray)
    for l in distances:
        for i in range(len(l)):
            if l[i] == -1:
                l[i] = 10**14
    for k in range(N):
        for i in range(N):
            for j in range(N):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    # print(distances)
    times = [[10**14] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if distances[i][j] <= horses[i][0]:
                times[i][j] = distances[i][j] / horses[i][1]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                times[i][j] = min(times[i][j], times[i][k] + times[k][j])
    # print(times)
    print("Case #%s: %s" % (case + 1, ' '.join('%.8f' % times[p[0] - 1][p[1] - 1] for p in points), ))
