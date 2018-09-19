fi = open("input.txt", "r")
fo = open("output.txt", "w")
n = int(fi.readline())
ans = 0

def check(a, b):
    a_s = str(a)
    b_s = str(b)
    if len(a_s) != len(b_s):
        return False
    k = 0
    res = b_s * 2
    for i in range(len(a_s)):
        t = 0
        for j in range(len(a_s)):
            if a_s[j] == res[i + j]:
                t += 1
        if t == len(a_s):
            return True
    return False

for i in range(n):
    a, b = fi.readline().split()
    a_i = int(a)
    b_i = int(b)
    ans = 0
    for j in range(a_i, b_i + 1):
        for k in range(j + 1, b_i + 1):
            if j != k and check(j, k):
                ans += 1
    fo.write("Case #" + str(i + 1) + ": " + str(ans) + "\n")