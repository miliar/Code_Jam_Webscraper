input = open("dance.in" , "r")
output = open("dance.out" , "w")
cases = int(input.readline())
for i in range(1, cases + 1):
    
    caseinfo = [int(x) for x in input.readline().split()]
    
    ans = 0
    norm = 0
    spec = 0
    lims = []
    
    n = caseinfo.pop(0)
    s = caseinfo.pop(0)
    p = caseinfo.pop(0)
    
    lims.append((p * 3) - 5)
    lims.append((p * 3) - 2)
    lims.append((p * 3) - 3)
    
    for l in range(len(lims)):
        if lims[l] < 0: lims[l] = 0

    for j in range(n):
        if caseinfo[j] > lims[0] and caseinfo[j] < lims[1]:
            spec += 1
        elif caseinfo[j] > lims[2]:
            norm += 1
    if s < spec:
        spec = s

    ans = norm + spec
    if p == 0:
        ans = n
    print "Case #" + str(i) + ": " + str(ans)
    output.write("Case #" + str(i) + ": " + str(ans) + "\n")
input.close()
output.close()
