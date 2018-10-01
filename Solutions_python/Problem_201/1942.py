from numpy import argmax


def solve(K, state):
    last = [-1, -1]
    for _ in range(K):
        idx = argmax(state)
        val = state[idx]-1
        state.pop(idx)
        last[0] = val - val // 2
        last[1] = val // 2
        state.insert(idx, last[1])
        state.insert(idx, last[0])
    return sorted(last, reverse=True)


for case in range(1, int(input()) + 1):
    N, K = tuple(map(int, input().split()))
    print('Case #{}:'.format(case), *solve(K, [N]), sep=' ')
