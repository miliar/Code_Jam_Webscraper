#!/usr/bin/python3
import sys
import os
import traceback
import code
from collections import *
from functools import *

if len(sys.argv) != 2:
    print ('Invalid args')
    sys.exit()
infile = sys.argv[1] 
if infile not in os.listdir('.'):
    print ('file not found!')
    sys.exit()
outfile = infile.replace('.in','.out')

f = open( infile, 'r' )
of = open( outfile, 'w' )

def output( *args, end='\n' ):
    print( ' '.join(map(str, args)), end=end )
    of.write( (' '.join(map(str,args)))+end )

def rev(s):
    return ''.join( c for c in reversed(s) )

def solCase( case ):
    h,w = map( int, f.readline()[:-1].split(' ') )
    ar = []
    for _ in range(h):
        ar.append( f.readline().strip() )
    c = 0
    for iy in range(h):
        for ix in range(w):
            flag = False
            change = True
            char = ar[iy][ix]
            if char == '.': continue
            for xx in range(ix):
                if ar[iy][xx] != '.':
                    flag = True
                    if char == '<': change = False
                    break
            for xx in range(ix+1,w):
                if ar[iy][xx] != '.':
                    flag = True
                    if char == '>': change = False
                    break
            for yy in range(iy):
                if ar[yy][ix] != '.':
                    flag = True
                    if char == '^': change = False
                    break
            for yy in range(iy+1,h):
                if ar[yy][ix] != '.':
                    flag = True
                    if char == 'v': change = False
                    break
            if not flag:
                output( "Case #%d: IMPOSSIBLE"%case )
                return
            if change: c += 1
    output( 'Case #%d: %d'%(case,c) )

for case in range(1,int(f.readline()[:-1])+1):
    solCase(case)
