
def solve(k):
    
    if k < 10: return k
    k1 = str(k)
    
    # Check for n
    tiny = True
    for idc in xrange(len(k1)-1):
        if int(k1[idc+1]) - int(k1[idc]) < 0:
            tiny = False
            break
    if tiny: return k

    # Else find next permutation
    tidy = ""
    for idc in xrange(len(k1)-1):
        if int(k1[idc+1]) <= int(k1[idc]):
            tidy = tidy + k1[idc] + "0"*(len(k1)-idc-1)
            break
        else:
            tidy = tidy + k1[idc]

    return int(tidy)-1

t = int(raw_input())
for i in xrange(t):
    n = raw_input()
    print "Case #{}: {}".format(i+1, solve(n))