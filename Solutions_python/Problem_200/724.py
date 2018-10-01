def is_tidy(n):
    if len(n) == 1:
        return True
    for i in range(len(n) - 1):
        if int(n[i]) > int(n[i + 1]):
            return False
    return True

def tidy_up(n):
    for i in range(len(n) - 1):
        if int(n[i]) > int(n[i + 1]):
            n = n[0:i] + str(int(n[i]) - 1) + '9' * (len(n) - i - 1)
    return n

def solve(n):
    while not is_tidy(n):
        n = tidy_up(n)
    return int(n)

t = int(input())
for i in range(t):
    print("Case #" + str(i + 1) + ":", end=' ')
    n = input()
    print(solve(n))