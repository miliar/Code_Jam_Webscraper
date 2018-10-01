numCases = int (raw_input())
for case in range (1, numCases+1):
    input = raw_input()
    N = int(input.split()[0])
    K = int(input.split()[1])
    min = 0; max = 0
    if N%2==0:
        max = N/2
        min = max-1
    else:
        min = max = (N-1)/2
    gaps = [min, max]
    i = 1
    while not i==K:
        gaps.sort()
        cur = gaps[len(gaps)-1]-1
        gaps.remove(cur+1)
        if cur%2==0:
            min = max = cur/2
        elif cur==0:
            min = max = 0
        else:
            max = (cur+1)/2
            min = max-1
        gaps.append(min)
        gaps.append(max)
        i = i+1
    print "case #"+str(case)+":", max, min
