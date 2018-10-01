def solve(N):
    cur = list(map(int, str(N)))
    for i in range(len(cur) - 1):
        if not cur[i] <= cur[i+1]:
            cur[i] -= 1
            cur = [9 if idx > i else val for idx, val in enumerate(cur)]
            return solve(''.join(map(str, cur)))
    return cur


for case in range(1, int(input()) + 1):
    print('Case #{}: {}'.format(
        case, ''.join(map(str, solve(int(input())))).lstrip('0')))
