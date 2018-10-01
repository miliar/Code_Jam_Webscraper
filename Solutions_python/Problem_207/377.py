from collections import *
for t in xrange(input()):
    colors = [['R','O','V'],['Y','G','O'],['B','G','V']]
    d = defaultdict(int)
    temp = map(int,raw_input().strip().split())
    order = ['R','O','Y','G','B','V']
    n = temp[0]
    del temp[0]
    for i in range(6):
        d[order[i]] = temp[i]
    del temp
    smalld = {'R':d['R'],'Y':d['Y'],'B':d['B']}
    temp2 = sorted(smalld.keys(),key = lambda x:smalld[x],reverse = True)
    if smalld[temp2[1]]+smalld[temp2[2]] < smalld[temp2[0]]:
        ans = 'IMPOSSIBLE'
    else:
        ans = list(temp2[0]*smalld[temp2[0]])
        now = temp2[1]
        for i in range(smalld[temp2[1]]):
            ans.insert(2*i+1,temp2[1])
        now = temp2[2]
        for i in range(smalld[temp2[2]]):
            ans.insert(len(ans)-(2*i),temp2[2])
            
    print "Case #{}: {}".format(t+1,"".join(ans))