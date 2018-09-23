# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems. 
from collections import deque
def flip(s,i,n):
    l = s[:]
    for j in range(i,i+n):
        l[j] *= -1
    return l
def stol(s):
    l =[]
    for i in s:
        if i == "+":
            l.append(1)
        else:
            l.append(-1)
    return l 
def done(l):
    for i in l:
        if i == -1:
            return False
    return True 
def calc(s, n): 
    if done(s):
        return 0
    queue = deque([[flip(s, i, n),1,i] for i in range(0,len(s)-n+1)])
    visited = set([tuple(l) for l in [s]+[q[0] for q in queue]])
    while queue:
        vertex,d,_ = queue.popleft()
        if done(vertex):
            return d
        else:
            for newflip,i in [[flip(vertex, i, n),i] for i in range(0,len(s)-n+1)]:
                if tuple(newflip) not in visited:
                    visited.add(tuple(newflip))
                    queue.append([newflip,d+1,i])  
        #print(queue)
    return "IMPOSSIBLE"
with open('input', 'r') as f:
    t = int(f.readline())
    for i in range(1, t + 1):
      s, n = f.readline().split(" ")  # read a list of integers, 2 in this case
      r = calc(stol(s), int(n))
      print("Case #{}: {}".format(i, r))
  # check out .format's specification for more formatting options
  
  
"""
3
---+-++- 3
+++++ 4
-+-+- 4
"""