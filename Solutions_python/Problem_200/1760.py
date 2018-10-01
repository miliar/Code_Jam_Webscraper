memo = {}


def tidy(n):
    if n in memo:
        return memo[n]
    if len(n) <= 1:
        return True
    res = ((int(n[0]) <= int(n[1])) and tidy(n[1:]))
    memo[n] = res
    return res


[cases] = [int(x) for x in raw_input().strip().split()]
out = open('output.txt', 'w')

for case in range(cases):
    # solving logic goes here
    n = int(raw_input().strip().split()[0])

    while(not tidy(str(n))):
        n -= 1

    s = "Case #"+str(case+1)+": "+str(n)+'\n'
    out.write(s)
    print(s)
