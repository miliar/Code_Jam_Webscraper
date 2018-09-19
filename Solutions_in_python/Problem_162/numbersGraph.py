#!/usr/bin/env python3

import sys, queue

def rev (k):
    return int(str(k)[::-1])

memory = {}
memory[1] = 1
q = queue.Queue()
q.put ((1, 1))

# BFS-based
def solve (N):

    #print (N)
    
    if N in memory:
        return memory[N]

    # Let's continue the bfs
    while (True):
        #print (q.qsize(), file=sys.stderr)
        # Get next item
        num, steps = q.get()
        #print (num, steps)
        # num + 1
        n1 = num+1
        if n1 not in memory:
            memory[n1] = steps+1
            q.put ((n1, steps+1))
        # rev(num)
        n2 = rev(num)
        if n2 not in memory:
            memory[n2] = steps+1
            q.put ((n2, steps+1))
        if num == N:
            return steps
        if n1 == N:
            return steps+1
        if n2 == N:
            return steps+1

if __name__ == "__main__":

    T = int (sys.stdin.readline())
    for t in range(1, T+1):
        N = int(sys.stdin.readline())
        print ("Case #%d: %d" % (t, solve(N)))

