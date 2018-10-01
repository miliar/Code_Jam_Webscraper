from math import ceil

def solve(a, b, mans):
    if mans == 1:
        return (int((b-a)/2) + (b-a)%2 - 1, int((b-a)/2 - 1))
    else:
        if (b-a)%2:
            t = mans%2
            t = 0 if t == 1 else 1
            return solve(a, int(b/2) + t, int(mans/2))
        else:
            return solve(a, int(b/2) + 1, int(mans/2))


t = int(input())

for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]

    l = solve(1, n+2, k)
    print ("Case #{0}: {1} {2}".format(i, l[0], l[1]))



    
