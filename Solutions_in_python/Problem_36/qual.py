from codejam import *
import math
import re

def problem1():
    basepath = '/home/ilya/workspace/codejam-python/'
    inputname = basepath + 'input.txt'
    outputname = basepath + 'output.txt'
    f_in = open(inputname)
    f_out = open(outputname, 'w')
    (L, D, N) = read_list(f_in)
    print L, D, N
    words = []
    for i in range(D):
        words.append(read_str(f_in))
    for testcase in range(N):
        pat = read_str(f_in)
        pat = pat.replace('(', '[').replace(')', ']')
        match = 0
        for w in words:
            if re.match(pat, w):
                match += 1
        print "Case #%i: %i" % (testcase+1, match)
        f_out.write("Case #%i: %i\n" % (testcase+1, match))

@codejam
def problem2(f):
    (H, W) = read_list(f)
    map = []
    map2 = []
    for i in range(H):
        map.append(read_list(f))
        map2.append([''] * W)
    l = 0
    for i in range(H):
        for j in range(W):
            x, y = i, j
            move = map2[x][y] == ''
            mark = []
            while move:
                mark.append((x,y))
                w = []
                if x != 0: w.append(map[x-1][y])
                if y != 0: w.append(map[x][y-1])
                if y != W-1: w.append(map[x][y+1])
                if x != H-1: w.append(map[x+1][y])
                if len(w) == 0 or min(w) >= map[x][y]:
                    move = False
                elif x != 0 and map[x-1][y] == min(w):
                    dx, dy = -1, 0
                elif y != 0 and map[x][y-1] == min(w):
                    dx, dy = 0, -1
                elif y != W-1 and map[x][y+1] == min(w):
                    dx, dy = 0, 1
                elif x != H-1 and map[x+1][y] == min(w):
                    dx, dy = 1, 0
                if move:
                    x += dx
                    y += dy
                    if map2[x][y] != '': move = False
            if map2[x][y] == '':
                map2[x][y] = chr(ord('a')+l)
                l += 1
            for (x1, y1) in mark:
                map2[x1][y1] = map2[x][y]
    s = ''
    for r in map2:
        s += '\n'
        s += ' '.join(r)
    return s

@codejam
def problem3(f):
    pat = 'welcome to code jam'
    L = len(pat)
    m = 10**4
    s = read_str(f)
    w = [0] * (L+1)
    w[0] = 1
    for c in s:
        for i in range(L):
            if c == pat[i]:
                w[i+1] += w[i]
                w[i+1] %= m
    return '%04i' % w[L]

problem3()