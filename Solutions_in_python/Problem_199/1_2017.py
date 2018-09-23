from collections import deque

[t, ] = [int(x) for x in input().split()]

def process_test(num):
    [line, k] = input().split()
    k = int(k)
    res = 0
    positions = deque()
    for i, char in enumerate(line):
        if not (len(positions) == 0) and positions[0] == i - k:
            positions.popleft()

        sign = 1 if char == '+' else 0
        sign += len(positions)

        if sign % 2 == 0:
            if i <= len(line) - k:
                positions.append(i)
                res += 1
            else:
                print("Case #", num, ": IMPOSSIBLE", sep='')
                return

    print("Case #", num, ": ", res, sep='')

for num in range(1, t + 1):
    process_test(num)