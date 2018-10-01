'''
Program to solve Problem B from Codejam 2010 1C
Danver Braganza
'''

import math
from Queue import deque

T = int(raw_input())

class memo:
    def __init__(self, fn):
        self._dict = {}
        self._fn = fn
    def __call__(self, *args):
        if args not in self._dict:
            self._dict[args] = self._fn(*args)
        return self._dict[args]

def midpoint(L, P, C):
    return math.e ** ((math.log(L) + math.log(P)) / 2)

@memo
def process(L, P, C):
    if L * C >= P: return 0
    if math.floor(midpoint(L, P, C)) == L: return 1
    if math.ceil(midpoint(L, P, C)) == P: return 1
    ans = min(process(math.floor(midpoint(L, P, C)), P, C ), 
              process(L, math.ceil(midpoint(L, P, C)), C)
              ) + 1
    return ans

for i in range(T):
    L, P, C = map(int, raw_input().split())
#   count = process(L, P, C)
    q = deque([])
    q.append((L, P, C, 0))
    while True:
        L, P, C, count = q.popleft()
        if L * C >= P: break
        if math.floor(midpoint(L, P, C)) == L:
            count += 1
            break
        if math.ceil(midpoint(L, P, C)) == P:
            count += 1
            break
        q.append((math.floor(midpoint(L, P, C)), P, C, count + 1,))
        q.append((L, math.ceil(midpoint(L, P, C)), C, count + 1,))
  
    print "Case #%d: %d" % (i + 1, count)


        
        
          

    


