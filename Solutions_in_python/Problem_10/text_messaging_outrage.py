from heapq import *

def solve(P, K, L, freq):
    assert(P * K >= L)
    assert(L == len(freq))
    key_heap = [(0, k) for k in xrange(K)]
    heapify(key_heap)
    freq.sort()
    key_presses = 0
    for letter_freq in reversed(freq):
        key = heappop(key_heap)
        if key[0] == P:
            raise Exception('no more space on keys')
        key = (key[0] + 1, key[1])
        heappush(key_heap, key)
        key_presses += key[0] * letter_freq
    return key_presses
        
if __name__ == '__main__':
    N = input()
    for i in xrange(N):
        P, K, L = (int(x) for x in raw_input().split())
        freq = [int(x) for x in raw_input().split()]
        print 'Case #%d: %d' % (i + 1, solve(P, K, L, freq))
        
