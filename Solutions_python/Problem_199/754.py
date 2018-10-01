
def solve(s, k):
    s = [c == '+' for c in s]
    flips = 0
    for i in range(len(s)-k+1):
        if not s[i]:
            s[i:i+k] = list(map(lambda x: not(x), s[i:i+k]))
            flips += 1
    if all(s):
        return flips
    else:
        return "IMPOSSIBLE"

# print(solve("---+-++-", 3))
# print(solve("+++++", 4))
# print(solve("-+-+-", 4))

t = int(input())
for i in range(1, t+1):
    line = input()
    s = line.split(" ")[0]
    k = int(line.split(" ")[1])
    print("Case #{}: {}".format(i, solve(s, k)))
