import math
from sets import Set
filein = open('A-large.in.txt', 'r')
fileout = open('A-large.out.txt', 'w')
 
T = int(filein.readline())
for t in range(T):
    fileout.write('Case #%d:\n' % (t + 1))
    # inp = [int(x) for x in filein.readline().split()]
    inp = [int(x) for x in filein.readline().split()]
    mat = []
    for i in range(inp[0]):
        temp = filein.readline().strip()
        mat.append([])
        for c in temp:
            mat[-1].append(c)
    s = Set()
    ans = []
    rowstart = -1
    for i in range(inp[0]):
        start = -1
        currow = []
        for j in range(inp[1]):
            cur = mat[i][j]
            if cur != '?' and cur not in s:
                currow  = currow + [cur]*(j-start)
                start = j
        if len(currow) > 0 and len(currow) < inp[1]:
            currow = currow + [currow[-1]]*(inp[1] - len(currow))
        if currow != []:
            ans = ans + [currow]*(i-rowstart)
            rowstart = i
    ans = ans + [ans[-1]]*(inp[0]-len(ans))



    # for tt in range(TT*2-1):
    #   inp.append()
    
    # result = []

    # for i in range(TT):
    #   seen = []
    #   for j in range(TT*2-1):
    #       seen.append(inp[j][i])
    #   val = sorted(seen)[2*i]
    #   # print seen
    #   # print val

    #   candidates = []
    #   for j in range(TT*2-1):
    #       if inp[j][i] == val:
    #           candidates.append(inp[j])
    #   if len(candidates) == 1:
    #       seen.append(val)
    #       # print candidates
    #       # print seen
    #       for x in candidates[0]:
    #           seen.remove(x)
    #       result = sorted(seen)
    # for u in result:
    for i in range(inp[0]):
        fileout.write(''.join(ans[i]))
        fileout.write("\n")     

    
 
filein.close()
fileout.close()