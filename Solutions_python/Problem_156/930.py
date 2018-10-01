#!/usr/bin/env python
from collections import deque


def special_minute(vals, new_val):
    aux = [v for v in sorted(vals, reverse=True)]
    if aux[0] == 1:
        return None
    aux[0] -= new_val
    aux.append(new_val)
    aux = [v for v in sorted(aux, reverse=True) ]

    if any(v < 0 for v in aux):
        print 'Problem'
    return aux


def eat_pancakes(vals):
    aux = [v-1 for v in vals if v > 0]
    if any(v < 0 for v in aux):
        print 'Problem'
    return aux


def bfs(vals, minutes=0):
    q = deque()
    q.append((vals, minutes))
    while q:
        node, minutes = q.popleft()
        if not node:
            continue
        if sum(node) == 0:
            return minutes
        node = [v for v in sorted(node, reverse=True)]
        last = (node[0]/2) + 1
        for v in xrange(2, last):
            other = special_minute(node, v)
            q.append((other, minutes+1))
        other = eat_pancakes(node)
        q.append((other, minutes+1))


def main():
    T = int(raw_input())
    for t in xrange(1, T+1):
        D = int(raw_input())
        vals = map(int, raw_input().split())
        
        minutes = bfs(vals)

        print 'Case #%d: %d' % (t, minutes)


if __name__ == "__main__":
    main()

