#!/usr/bin/env python3
# coding: utf-8

N = 4

def win(b):
    for i in range(len(b)):
        if b[i].count('O') == N: return 'O won'
        if b[i].count('X') == N: return 'X won'
        if b[i].count('O') == N-1 and 'T' in b[i]: return 'O won'
        if b[i].count('X') == N-1 and 'T' in b[i]: return 'X won'
    return None

def draw(b):
    for i in range(N):
        if '.' in b[i]: return False
    return True

def solve(b):
    a = list(zip(*b))
    b.append([b[i][i] for i in range(N)])
    b.append([b[i][N-i-1] for i in range(N)])
    if win(a): return win(a)
    if win(b): return win(b)
    if draw(a): return 'Draw'
    return 'Game has not completed'

for case in range(int(input())):
    if case: input()
    b = []
    for i in range(N): b.append(input())
    print('Case #{}: {}'.format(case+1, solve(b)))
