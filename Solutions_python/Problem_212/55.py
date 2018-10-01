import math
from multiprocessing import Pool

def solve(args):
    N, P, G = args
    G = map(lambda x : x % P, G)
    count = [0] * P
    ans = 0
    for g in G:
        count[g] += 1
    if P == 2:
        ans = count[0] + (count[1] + 1) / 2
    elif P == 3:
        ans = min(count[1], count[2])
        count[1] -= ans
        count[2] -= ans
        ans += (count[1] + 2) / 3 + (count[2] + 2) / 3
        ans += count[0]
    else:
        ans = min(count[1], count[3])
        count[1] -= ans
        count[3] -= ans
        ans += count[2] / 2
        ans += count[1] / 4
        ans += count[3] / 4
        count[2] = count[2] % 2
        count[3] = count[3] % 4
        count[1] = count[1] % 4
        if count[2] > 0 and count[1] > 1:
            ans += 1
            count[2] -= 1
            count[1] -= 2
        if count[2] > 0 and count[3] > 1:
            ans += 1
            count[2] -= 1
            count[3] -= 2
        if sum(count[1:]) > 0:
            ans += 1
        ans += count[0]
    return ans

def formatter(arg):
    return 'Case #{0}: {1}'.format(arg[0] + 1, arg[1])

def input_gen(T):
    for i in xrange(1, T + 1):
        N, P = map(int, raw_input().strip().split())
        G = map(int, raw_input().strip().split())
        yield N, P, G

def main():
    CORES = 1
    p = Pool(CORES)
    T = input()
    print '\n'.join(map(formatter, enumerate(
        p.map(solve, input_gen(T), T / CORES)
        # p.map(solve, input_gen(T), 1)
    )))
    p.map(solve, input_gen(T))

def main1():
    print(solve((3, 4, [1, 1, 1, 1, 1, 1, 1, 1, 1])))

if __name__ == '__main__':
    main()
    # main1()
