def issorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def solve(ns):
    l = map(int,ns)
    while not issorted(l):
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                l[i]-=1
                l[i+1:] = [9]*(len(l)-i-1)
                #print "trying",nl
    return "".join(map(str,l)).lstrip("0")

for i in range(input()):
    print "Case #{}: {}".format(i+1,solve(raw_input().strip()))
