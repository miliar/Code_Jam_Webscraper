from itertools import groupby
import re


def ccnt(s):
    current = [s[0],1]
    out = [current]
    ans = []
    for c in s[1:]:
        if c == current[0]:
            current[1] += 1
        else:
            current = [c, 1]
            out.append(current)
    for m in out:
        ans.append(m[1])
    return ans

for case in range(int(raw_input())):
    N = input()
    ipt = []

    cnt = 0
    for i in range(N):
        ipt.append(raw_input())
    
    if ''.join(c for c, _ in groupby(ipt[0])) != ''.join(c for c, _ in groupby(ipt[1])):
        print "Case #%d: %s" % (case+1, "Fegla Won")
        continue
    
#     for c in ''.join(c for c, _ in groupby(ipt[0])):
#         print ccnt(ipt[0])
#         #cnt0.append()
#         #cnt1.append(len(list(g)) for g in groupby(ipt[1]))
    
    cnt0 = ccnt(ipt[0])
    cnt1 = ccnt(ipt[1])
 
#     print "cnt0:%s, cnt1:%s" % (cnt0, cnt1)
#     
#     
#     
#     
    for i in range(len(cnt0)):
        avg = (cnt0[i]+ cnt1[i])/2
        cnt += abs(cnt0[i] - avg) + abs(cnt1[i] - avg)
        

    print "Case #%d: %d" % (case+1, cnt)