#!/usr/bin/env python2.7
from __future__ import print_function
import operator as op

def read_case():
    tokens = raw_input().split()
    L, t, N, C = map(int, tokens[:4])
    a = map(int, tokens[4:])
    return (L, t, N, C, a)

def solve(case):
    L, t, N, C, a = case 
    full = N / C
    last = a[:N % C]
    distC = sum(a)
    time = 2 * (distC * full + sum(last))
    if t >= time:
        return time
    behind = t / (2 * distC) 
    numleft = [max(0, full - behind)] * len(a)
    for i in xrange(len(last)):
        numleft[i] += 1
    t_left = t - behind * 2 * distC
    cur_idx = 0
    while t_left > 0 and 2 * a[cur_idx] <= t_left:
        t_left -= 2 * a[cur_idx]
        numleft[cur_idx] -= 1
        cur_idx += 1
    if t_left > 0:
        numleft[cur_idx] -= 1
        a.append(a[cur_idx] - t_left / 2)
        numleft.append(1)
    dists = sorted(zip(a, numleft), key=op.itemgetter(0))
    stars_left = sum(d[1] for d in dists)
    while stars_left > 0 and L > 0:
        assgn = min(dists[-1][1], L)
        time -= assgn * dists[-1][0]
        L -= assgn
        stars_left -= assgn
        dists.pop()
    return time

T = int(raw_input())
for caseidx in xrange(1, T+1):
    print("Case #{}: {}".format(caseidx, solve(read_case())))
