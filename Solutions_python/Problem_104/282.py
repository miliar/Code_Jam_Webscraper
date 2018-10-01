#!/usr/bin/env python

visited = set()
def dfs(a,b,sa,sb,ns,i):
    global visited
    visited.add((sa,sb))

    if sa > 0 and sa == sb:
        return a,b
    elif i >= len(ns):
        return False
    else:
        ret = dfs(a,b,sa,sb,ns,i+1)
        if ret != False:
            return ret
        if (sa+ns[i],sb) not in visited:
            ret = dfs(a+[ns[i]],b,sa+ns[i],sb,ns,i+1)
            if ret != False:
                return ret
        if (sa,sb+ns[i]) not in visited:
            ret = dfs(a,b+[ns[i]],sa,sb+ns[i],ns,i+1)
            if ret != False:
                return ret
        return False

t = int(input())
for case in range(1,t+1):
    visited = set()
    ns = list(map(int,(input().strip().split())[1:]))
    ret = dfs([],[],0,0,ns,0)
    print('Case #{}:'.format(case))
    if ret == False:
        print('Impossible')
    else:
        for i in range(len(ret[0])):
            print(ret[0][i], end='')
            if i < len(ret[0])-1:
                print(' ', end='')
        print()
        for i in range(len(ret[1])):
            print(ret[1][i], end='')
            if i < len(ret[1])-1:
                print(' ', end='')
        print()
