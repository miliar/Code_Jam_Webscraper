#!/usr/bin/python


def solve(n,k):
    if k == 1:
        spots_left = n-1
        a = spots_left/2
        b = spots_left - a
        return "{} {}".format(max(a,b),min(a,b))
    elif (n-1)%2 == 0 and (k-1)%2 == 0:
        return solve( (n-1)/2, (k-1)/2 )
    elif (n-1)%2 == 1 and (k-1)%2 == 0:
        return solve( (n-1)/2, (k-1)/2)
    elif (n-1)%2 == 0 and (k-1)%2 == 1:
        return solve( (n-1)/2, (k-1)/2 + 1)
    elif (n-1)%2 == 1 and (k-1)%2 == 1:
        return solve((n-1)/2 + 1, (k-1)/2 + 1)


PATH = "/mnt/c/Users/mannes/Downloads/C-small-1-attempt0.in"
f = open(PATH, "r")
lines = f.readlines()
instances = [l.strip().split() for l in lines[1:]]
instances = [map(int, l) for l in instances]

for n in range(len(instances)):
    i = instances[n]
    print "Case #{}: {}".format(n + 1, solve(i[0],i[1]))

