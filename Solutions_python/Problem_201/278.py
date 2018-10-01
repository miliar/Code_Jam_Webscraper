# Bathroom Stalls

def solve(n, k):
    v = [[n, 1]]
    while len(v) > 0:
        (n, p) = v.pop(0)
        if k <= p:
            return [n / 2, (n - 1) / 2]
        k -= p
        for x in [n / 2, (n - 1) / 2]:
            flag = False
            for i in range(len(v)):
                if x == v[i][0]:
                    v[i][1] += p
                    flag = True
            if not flag:
                v.append([x, p])

cases = int(raw_input())
for case in range(1, cases + 1):
    (n, k) = map(int, raw_input().split(' '))
    print "Case #" + str(case) + ": " + " ".join(map(str, solve(n, k)))
