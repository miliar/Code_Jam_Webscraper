from collections import deque

def fitness(s):
    res = 0
    for char in s:
        if char == '+':
            res += 1
    return res

def flip(s):
    res = []
    for char in s:
        if char == '+':
            res.append('-')
        elif char == '-':
            res.append('+')
    return ''.join(res)

def calculate_flips(initial, k):
    n = len(initial)
    seen = set()
    queue = deque()
    seen.add(initial)
    queue.append(initial)
    flips = 0
    while queue:
        m = len(queue)
        while m > 0:
            current = queue.popleft()
            if fitness(current) == n:
                return flips
            for j in xrange(n-k+1):
                flipped = current[:j] + flip(current[j:j+k]) + current[j+k:]
                if flipped not in seen:
                    seen.add(flipped)
                    queue.append(flipped)
            m -= 1
        flips += 1

    return 'IMPOSSIBLE'

T = int(raw_input())
for i in xrange(1, T+1):
    row = raw_input().split()
    initial = row[0]
    k = int(row[1])

    num_flips = calculate_flips(initial, k)

    print "Case #{}: {}".format(i, num_flips)    
