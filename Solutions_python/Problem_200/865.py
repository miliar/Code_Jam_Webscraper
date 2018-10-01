#!/usr/bin/env python3

def solve(case_n, N):
    N = [int(n) for n in str(N)]
    i = 0
    while True:
        if i == len(N)-1:
            break
        if N[i] > N[i+1]:
            N[i] -= 1
            for j in range(i+1, len(N)):
                N[j] = 9
            i = 0
        else:
            i += 1
    return int("".join(map(str, N)))

def main():
    t = int(input())
    for case_n in range(1, t+1):
        N = int(input())
        res = solve(case_n, N)
        print("Case #{}: {}".format(case_n, res))

if __name__ == "__main__":
    main()
