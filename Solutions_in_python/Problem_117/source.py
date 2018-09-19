#!/usr/bin/env python

def figure_out_single_cell(x,y,l,cx,cy):
    flag = True
    for i in xrange(0,x):
        if l[i][cy]>l[cx][cy]:
            flag=False
            break
    if flag:
        return True
    flag = True
    for i in xrange(0,y):
        if l[cx][i]>l[cx][cy]:
            flag=False
            break
    if flag:
        return True
    return False

def figure_out(x,y,l):
    for i in xrange(0,x):
        for j in xrange(0,y):
            if figure_out_single_cell(x,y,l,i,j) == False:
                return False
    return True

def main():
    n=int(raw_input())
    for i in xrange(0,n):
        s=raw_input()
        [x,y]=[int(n) for n in s.split(' ')]
        game_map=[]
        for j in xrange(0,x):
            s=raw_input()
            l=[int(n) for n in s.split(' ')]
            game_map.append(l)
        if figure_out(x,y,game_map):
            print('Case #%d: YES'%(i+1,))
        else:
            print('Case #%d: NO'%(i+1,))
        
main()