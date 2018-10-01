#!/usr/bin/env python3

# !py a.py < a.in > a.out



def main():
    t = int(input())
    for i in range(1, t+1):
        #input
        args = map(int, input().split())
        
        #comput
        ans = solve(*args)
        
        #output
        print('Case #%d:' % i, ans)
    


def solve(hd0, ad, hk, ak, b, d):
    # There are probably trick cases where you will figure out that a move is useless.
    state = hd0, hd0, ad, hk, ak
    
    def Attack(hd0, hd, ad, hk, ak):
        return hd0, hd, ad, hk-ad, ak

    def Buff(hd0, hd, ad, hk, ak):
        return hd0, hd, ad+b, hk, ak

    def Cure(hd0, hd, ad, hk, ak):
        return hd0, hd0, ad, hk, ak

    def Debuff(hd0, hd, ad, hk, ak):
        return hd0, hd, ad, hk, max(0,ak-d)

    def KnightTurn(hd0, hd, ad, hk, ak):
        return hd0, hd-ak, ad, hk, ak

    def victory(hd0, hd, ad, hk, ak):
        return hk <= 0

    def defeat(hd0, hd, ad, hk, ak):
        return hd <= 0

    dragon_actions = [Attack, Cure]
    if b:
        dragon_actions.append(Buff)
    if d:
        dragon_actions.append(Debuff)

    def bfs(state):
        seen = set()
        queue = [state]
        turns = 0
        while queue:
            queue1 = []
            for st in queue:
                if victory(*st):
                    return turns
                elif defeat(*st):
                    continue
                for action in dragon_actions:
                    st1 = KnightTurn(*action(*st))
                    if st1 in seen:
                        continue
                    seen.add(st1)
                    queue1.append(st1)
            queue = queue1
            turns += 1
        return "IMPOSSIBLE"
    return bfs(state)






###################


from sys import stdin, stdout, stderr
import operator as op
from functools import *
memoize = lru_cache(None)
from itertools import *
from collections import *
chainit = chain.from_iterable
flatten = chain.from_iterable


iget = op.itemgetter

get0 = iget(0)
get1 = iget(1)
get2 = iget(2)





###############

main()

