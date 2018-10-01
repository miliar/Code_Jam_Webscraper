import sys

from itertools import islice

Ts, *data = sys.stdin.read().split()

for T, s in enumerate(islice(data, 1, len(data), 2)):
    friends = 0
    cnt = 0
    for i, v in enumerate(map(int, s)):
        insuf = v and max(0, i - cnt)
        cnt += insuf + v
        friends += insuf
    print("Case #{}: {}".format(T+1, friends))
    
