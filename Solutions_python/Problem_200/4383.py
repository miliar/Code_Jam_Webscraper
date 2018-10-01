# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for tc in range(1, t + 1):
    x = list(input().strip())
    n = len(x)
    while not all(x[i] <= x[i + 1] for i in range(n - 1)):
        for idx, char in enumerate(x):
            if idx == n - 1:
                break
            if x[idx] > x[idx + 1]:
                x[idx] = chr(ord(x[idx]) - 1)
                x = x[:idx + 1] + ['9']*(n - idx - 1)
                #print(x)
                break
    for idx, char in enumerate(x):
        if char == '0':
            x = x[idx + 1:]
    print("Case #{}: {}".format(tc, ''.join(x)))
