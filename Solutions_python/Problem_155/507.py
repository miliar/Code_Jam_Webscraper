#!/usr/bin/python2

def main():
    n = input()
    for t in range(n):
        _, num = raw_input().split()
        print 'Case #{}: {}'.format(t + 1, solve(num))

def solve(num):
    l = map(int, list(num))
    num_ovating = 0
    num_needed = 0
    for n, people in enumerate(l):
        if num_ovating < n:
            to_add = n - num_ovating
            num_needed += to_add
            num_ovating += to_add
        num_ovating += people
    return num_needed

main()
