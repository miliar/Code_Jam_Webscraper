
def war(lst1, lst2):
    count = 0
    # O(n^2) for now
    while lst1:
        n = lst1[-1]
        lst1 = lst1[:-1]
        if n > lst2[-1]:
            lst2 = lst2[1:]
            count += 1
        else:
            i = 0
            while lst2[i] < n:
                i += 1
            lst2 = lst2[:i] + lst2[i+1:]
    return count
    
def memo(f):
    cache = {}
    def wrap(i,j):
        if (i,j) not in cache:
            cache[(i,j)] = f(i,j)
        return cache[(i,j)]
    return wrap
    
def lying_war(lst1, lst2):
    # Either lie to remove largest, or lie to remove smallest and earn a point
    # if smaller than smallest then can only remove largest
    # if bigger than smallest then can lie
    @memo
    def score(i, j):
        if i == j:
            return 0
        n = lst1[len(lst2) - (j-i)]
        if n < lst2[i]:
            return score(i, j-1)
        return max(score(i,j-1), 1+score(i+1,j))
    return score(0, len(lst2))
  
import sys
sys.setrecursionlimit(10000)
  
for case in range(input()):
    n = input()
    lst1 = map(float, raw_input().split())
    lst2 = map(float, raw_input().split())
    lst1.sort()
    lst2.sort()
    print "Case #%d: %d %d" % (case+1, lying_war(lst1, lst2), war(lst1, lst2))
    