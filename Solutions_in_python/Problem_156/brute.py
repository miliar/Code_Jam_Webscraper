from functools import lru_cache

@lru_cache(maxsize=None)
def solve(state):
    clean = [x for x in state if x is not 0]
    clean.sort()
    clean.reverse()
    if len(clean) == 0:
        return 0
    result = 1000
    result = min(result, solve(tuple([x-1 for x in clean])))
    first = clean[0]
    for k in range(2, first-1):
        result = min(result, solve(tuple([k, first - k] + clean[1:])))
    return (result + 1)

if __name__ == '__main__':
    T = int(input())
    for I in range(1, T+1):
        result = 0
        d = int(input())
        state = [int(x) for x in input().split()]
        result = solve(tuple(state))
        print("Case #%d: %d" % (I, result))
