#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:17:31 2017

@author: barnrang
"""


def update(type, x, y):
    if type == '+':
        diagl[(x - y)+(n-1)] += 1
        diagr[x+y-2] += 1
    elif type == 'x':
        hori[x - 1] +=1
        verti[y - 1] +=1
    else:
        diagl[(x-y)+(n-1)] += 1
        diagr[x+y-2] += 1
        hori[x - 1] +=1
        verti[y - 1] +=1
score = {'.':0,'+':1,'x':1,'o':2}
             
             
t=int(input())
for i in range(1, t + 1):
    n,m = [int(x) for x in input().split(' ')]
    table = [['.' for lol in range(n)] for kuy in range(n)]
    out = [['.' for lol in range(n)] for kuy in range(n)]
    verti = [0 for hh in range(n)]
    hori = [0 for hh in range(n)]
    diagl = [0 for hh in range(2*n - 1)]
    diagr = [0 for hh in range(2*n - 1)]
    change = []
    point = 0
    for j in range(m):
        type, x, y = input().split(' ')
        x, y = int(x), int(y)
        table[x-1][y-1] = type
        out[x-1][y-1] = type
        point += score[type]
        update(type, x, y)
    for hoz in range(n):
        for ver in range(n):
            if hori[hoz] == 0 and verti[ver] == 0:
                if out[hoz][ver] == '+':
                    if ['+',hoz + 1, ver + 1] in change:
                        change.remove(['+',hoz + 1, ver + 1])
                    change.append(['o',hoz + 1, ver + 1])
                    out[hoz][ver] = 'o'
                else:
                    change.append(['x',hoz + 1, ver + 1])
                    out[hoz][ver] = 'x'
                update('x',hoz + 1,ver + 1)
                point += 1
    store = [0 for hhh in range(n)]
    head = 0
    tail = n-1
    for l in range(n):
        if l%2==0:
            store[l] = head
            head += 1
        else:
            store[l] = tail
            tail -= 1
    for dx in store:
        for dy in range(n):
            if diagl[dx - dy + n - 1] == 0 and diagr[dx + dy] == 0:
                if out[dx][dy] == 'x':
                    if ['x', dx + 1, dy + 1] in change:
                        change.remove(['x', dx + 1, dy + 1])
                    out[dx][dy] = 'o'
                    change.append(['o', dx + 1, dy + 1])
                else:
                    change.append(['+', dx + 1, dy + 1])
                    out[dx][dy] = '+'
                update('+',dx + 1,dy + 1)
                point += 1
    #finish filling
    #next upgrading
#    for xco in range(1, n+1):
#        for yco in range(1, n+1):
#            ele = out[xco-1][yco-1]
#            if  ele == '.' or ele == 'o':
#                continue
#            elif ele == '+':
#                if verti[yco-1] == 0 and hori[xco -1] == 0:
#                    out[xco-1][yco-1] = 'o'
#                    update('x',xco,yco)
#                    if ['+',xco,yco] in change:
#                        change.remove(['+',xco,yco])
#                    change.append(['o',xco,yco])
#                    point += 1
#            else:
#                if diagl[n-1-(xco-yco)] == 0 and diagr[xco+yco-2] == 0:
#                    out[xco-1][yco-1] = 'o'
#                    update('+',xco,yco)
#                    if ['+',xco,yco] in change:
#                        change.remove(['x',xco,yco])
#                    change.append(['o',xco,yco])
#                    point += 1
#    for k in range(n):
#        for model in out[k]:
#            print(model, end='')
#        print()
#    count = 0
#    newpoint = 0
#    for l in range(n):
#        for p in range(n):
#            newpoint += score[out[l][p]]
#            if table[l][p] != out[l][p]:
##                change.append([out[l][p], l+1, p+1])
#                count += 1
#    if count != len(change) or point != newpoint:
#        print('bye')
#        break
#    print(diagl,diagr)
    for chr in change:
        table[chr[1] - 1][chr[2] - 1] = chr[0]
    if table != out:
        print('boom')
        break
    print('Case #{}: {} {}'.format(i, point, len(change)))
    for ch in change:
        print('{} {} {}'.format(ch[0],ch[1],ch[2]))