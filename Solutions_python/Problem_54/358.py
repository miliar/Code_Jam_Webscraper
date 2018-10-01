def gcd(a, b):
    if a > b: a,b = b,a 
    if a == 0: 
        return b
    else:   
        return gcd(a, b%a)

def solve(times):
    t = min(times)
    diffs = [ ot - t for ot in times ]
    d = max(diffs)
    for x in diffs:
        if x == 0: continue
        d = gcd(x, d)

    return -t % d

cases = int(input())
for i in range(cases):
     ans = solve([int(x) for x in input().split()[1:]])
     print("Case #" + str(i+1) + ": " + str(ans))
