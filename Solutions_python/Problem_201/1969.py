def max_heapify(heap, ind, elem):
    if ind >= len(heap): return
    l, r = 2 * ind + 1, 2 * ind + 2
    largest = l if l < elem and heap[l] > heap[ind] else ind
    if r < elem and heap[r] > heap[largest]: largest = r
    if largest != ind:
        heap[ind], heap[largest] = heap[largest], heap[ind]
        max_heapify(heap,largest, elem)

def insert(heap, ind, val):
    heap[ind] = val
    parent = (ind-1)//2
    while parent >= 0 and heap[ind] > heap[parent]:
        heap[parent], heap[ind] = heap[ind], heap[parent]
        parent, ind = (parent-1)//2, parent

def choose(N, K):
    if N >= 8:
        prev = 1<<((N-1).bit_length()-1)
        before = prev/2
        if N > prev + before and K >= prev: return 0, 0
        elif prev + before >= N and K >= before + (N - prev + 1): return 0, 0
    size = 1<<(K).bit_length()
    maxHeap = [-1 for _ in range(size + 1)]
    maxHeap[0] = N
    res, elems = N, 1
    for k in range(K):
        res = maxHeap[0]
        if res == 1: break
        maxHeap[0], maxHeap[elems-1] = maxHeap[elems-1], -1 
        elems -= 1
        max_heapify(maxHeap, 0, elems)
        insert(maxHeap, elems, res//2); elems += 1
        insert(maxHeap, elems, max((res-1)//2, 0)); elems += 1
    return res//2, max((res-1)//2, 0)

"""
for i in range(60, 70):
    res = choose(117, i)
    print("Case #%i: %i %i" % (i, res[0], res[1]))
"""


T = int(input())
for t in range(T):
    N, K = [int(i) for i in input().split()]
    res = choose(N, K)
    print("Case #%i: %i %i" % (t+1, res[0], res[1]))

