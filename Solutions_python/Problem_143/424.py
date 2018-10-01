#!/usr/bin/env python3

################################################################################

def read_int():
    return int(input())

def read_words():
    return input().split()

def read_ints():
    return list(map(int,read_words()))

def read_floats():
    return list(map(float,read_words()))

################################################################################

def quantify(iterable, pred=bool):
    "Count how many times the predicate is true"
    return sum(map(pred, iterable))

def solve(a,b,k):
    return quantify( ( (i,j,k) for i in range(a) for j in range(b) ), lambda x: x[0]&x[1] < x[2] )


if __name__ == "__main__":
    T = read_int()
    for c in range(T):
        A,B,K = read_ints()
        R = solve(A,B,K)
        print("Case #{}: {}".format(c+1,R))
