import heapq
from math import ceil 

def insert_range(h, qm, r, n):
    if r in qm:
        qm[r] += n
    else:
        qm[r] = n
        heapq.heappush(h, -r)

def stall_man_was_right(stalls, people):
    if stalls == people:
        return (0, 0)

    h = [-stalls]
    qm = {stalls: 1}

    eliminated = 0
    while True:
        current = -heapq.heappop(h)
        q = qm[current]
        eliminated += q
        if eliminated >= people: 
            return (current//2, ceil(current/2)-1)

        del qm[current] # Just took all these ranges out
        
        if current&1:
            new_range = (current-1)//2
            insert_range(h, qm, new_range, q*2)
        else:
            # Have to do uneven split
            bigger_new_range = current//2
            insert_range(h, qm, bigger_new_range, q)

            smaller_new_range = (current//2)-1
            insert_range(h, qm, smaller_new_range, q)


T = int(input())
for t in range(1, T+1):
    stalls, people = input().split(' ')
    mini, maxi = stall_man_was_right(int(stalls), int(people))
    print('Case #', t, ': ', mini, ' ', maxi, sep='') 
