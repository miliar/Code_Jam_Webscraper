import heapq

with open('/Users/shawn/Documents/python_proj/codejam/C-small-2-attempt1.in', 'r') as f:
    cases = int(f.readline())
    lines = f.readlines()

for case in range(cases):
    N, K = lines[case].strip().split(" ")
    N = int(N)
    K = int(K)

    heap = []
    heapq.heappush(heap, -N)
    max_s = 0
    min_s = 0
    if N < (K/0.6):
        max_s = 0
        min_s = 0
    else:
        for i in range(K):
           dis = -heapq.heappop(heap)
           if dis <= 1:
               max_s = 0
               min_s = 0
               break
           elif dis % 2 == 0:
               new_dis = dis / 2
               max_s = new_dis
               min_s = new_dis - 1
               heapq.heappush(heap, -max_s)
               if min_s:
                   heapq.heappush(heap, -min_s)
           else:
               new_dis = dis / 2
               max_s = min_s = new_dis
               heapq.heappush(heap, -max_s)
               heapq.heappush(heap, -min_s)


    print "Case #" + str(case + 1) + ": " + str(max_s) + " " + str(min_s)