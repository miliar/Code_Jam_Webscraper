# coding: utf-8

import Queue

def solve(idx, state, K):
    L = len(state)
    dp = range(1 << L)
    for i, v in enumerate(dp):
        dp[i] = -1
    init_state = 0
    for v in state:
        init_state <<= 1
        if v == '+':
            init_state += 1
    mask = (1 << K) - 1
    dp[init_state] = 0
    q = Queue.Queue()
    q.put(init_state)
    while not q.empty():
        current_state = q.get()
        if current_state + 1 == 1 << L:
            print 'Case #{0}: {1}'.format(idx, dp[current_state])
            return
        for i in range(L - K + 1):
            next_state = current_state ^ (mask << i)
            if dp[next_state] == -1:
                dp[next_state] = dp[current_state] + 1
                q.put(next_state)
    print 'Case #{0}: IMPOSSIBLE'.format(idx)

def main():
    T = raw_input()
    T = int(T)
    for i in range(1, T + 1):
        s = raw_input()
        s = s.split(' ')
        solve(i, s[0].strip(), int(s[-1].strip()))

if __name__ == '__main__':
    main()
