def is_tidy(n):
    ls = str(n)
    if len(ls) < 2:
        return True
    i = 1
    while i < len(ls):
        if ls[i] < ls[i-1]:
            return False
        i += 1
    return True

def reduce(s):
    i = len(s) - 1
    while i > 0:
        if s[i-1] < s[i]:
            break
        i -= 1
    if i == 0:
        if s[0] == '1':
            return "9"*(len(s) - 1)
        return str(int(s[0]) - 1) + "9"*(len(s) - 1)
    return "".join(s[:i]) + str(int(s[i]) - 1) + "9"*(len(s) - i - 1)
    

def solve(n):
    for i in range(10):
        if is_tidy(n-i):
            return n - i
    ls = str(n)
    fe = 0
    while ls[fe] <= ls[fe + 1]:
        fe += 1
    return reduce(ls[:(fe + 1)]) + "9"*(len(ls) - fe - 1) 


T  = int(input().strip())
for i in range(T):
    n = int(input().strip())
    print("Case #" + str(i + 1) + ":", solve(n))