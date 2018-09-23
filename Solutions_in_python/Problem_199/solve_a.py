"""

---+-++- 3
++++-++-
+++++---
++++++++

"""

t = int(raw_input())

def is_valid(s):
    return ('-' not in s)

def flip(s, start, lenght):
    if start+lenght > len(s):
        return s

    for idx in range(start, start+lenght):
        if s[idx] == '+':
            s[idx] = '-'
        elif s[idx] == '-':
            s[idx] = '+'
    return s

def solve(tcount):
    flip_count = 0
    s, k = raw_input().split(' ')
    k = int(k)
    s = list(s)

    for idx in range(len(s)):
        if s[idx] == '-':
            s = flip(s, idx, k)
            flip_count += 1
            if is_valid(s):
                print("Case #{}: {}".format(tcount+1, flip_count))
                return

    if is_valid(s):
        print("Case #{}: {}".format(tcount+1, flip_count))
    else:
        print("Case #{}: IMPOSSIBLE".format(tcount+1))
    return

for t_idx in range(t):
    solve(t_idx)
