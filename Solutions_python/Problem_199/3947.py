from collections import defaultdict, deque

def flip(s):
    return s.replace("-", "=").replace("+", "-").replace("=", "+")

def neighbors(v,k):
    n = []
    for i in range(0, len(v)-k+1):
        n.append(v[:i] + flip(v[i:i+k]) + v[i+k:])
    return n

t = int(raw_input())
for i in range(1, t+1):
    s, k_string = raw_input().split(" ")
    length = len(s)
    k = int(k_string)
    #print("Case #{}: {} {}".format(i, s, k))
    #print("neighbors(s, k): {}".format(neighbors(s,k)))

    marked = defaultdict(lambda: False)
    distance = defaultdict(lambda: -1)
    
    marked[s] = True
    distance[s] = 0

    q = deque()
    q.append(s)

    while len(q) > 0:
        v = q.popleft()
        n = neighbors(v,k)
        for u in n:
            if not marked[u]:
                if distance[u] > distance[v] + 1:
                    distance[u] = distance[v] + 1
                elif distance[u] == -1:
                    distance[u] = distance[v] + 1
                marked[u] = True
                q.append(u)

    result = distance["+"*length]
    if result == -1:
        result = "IMPOSSIBLE"
    print("Case #{}: {}".format(i, result))
