
def solve(s, k):
    res = 0
    for i in range(len(s) - k + 1):
        if s[i] == "-":
            res += 1
            for j in range(k):
                if s[i + j] == "-":
                    s[i + j] = "+"
                else:
                    s[i + j] = "-"
    if "-" in s:
        return "IMPOSSIBLE"
    else:
        return res

tests = int(input())

for test in range(tests):
    s_before, k = [x for x in input().split()]
    k = int(k)
    s_array = []
    for i in range(len(s_before)):
        s_array.append(s_before[i])
    res = solve(s_array, k)
    print("Case #%d:" % (test + 1), res)
