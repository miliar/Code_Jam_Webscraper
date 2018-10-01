# -*- coding: utf-8 -*-
import sys
from collections import deque

getline=sys.stdin.readline;

def BIT(c, i):
    return ((c>>i)&1)

h2i={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

def chesscheck(B, xs, ys, sz):
    if sz==1:
        if B[ys][xs]==2:
            return 0
        return 1

    try:
        for y in range(ys, ys+sz):
            if B[y][xs]==2:
                raise StopIteration()
            if ( (y>ys) and (B[y][xs]==B[y-1][xs]) ):
                raise StopIteration()

            for x in range(xs+1, xs+sz):
                if B[y][x]==2:
                    raise StopIteration()
                if B[y][x]==B[y][x-1]:
                    raise StopIteration()

    except StopIteration:
        return 0
    return 1

def fill(B, xs, ys, sz, v):
    if sz==1:
        B[ys][xs]=v
    else:
        for j in range(ys, ys+sz):
            for i in range(xs, xs+sz):
                B[j][i]=v
    return B

T=int(getline());
print >> sys.stderr, 'T={0}'.format(T)

for idx in range(T):
    print >> sys.stderr, '=== {0} ==='.format(idx+1);

    # récupération des variables
    V=getline().split(" ");
    M=int(V[0]);
    N=int(V[1]);
    B=[];
    for i in range(M):
        B.append([]);
        V=getline();
        for j in range(N/4):
            for k in range(4):
                B[i].append(BIT(h2i[V[j]], 3-k));

    # affichage des variables
    print >> sys.stderr, ' M={0}'.format(M);   # heuteur (nombre de lignes)
    print >> sys.stderr, ' N={0}'.format(N);   # largeur (nombre de colonnes)
    print >> sys.stderr, ' B={0}'.format(B);   # écorce (liste de M lignes et N colonnes)

    # recherche et affichage de la solution
    print 'Case #{0}:'.format(idx+1),
    nb=[];
    for sz in range(min(M, N), 0, -1):  # pour chaque taille en commencant par les plus grandes
        nbi=0;
        for yoff in range(M-sz+1):      # pour chaque position en y de la possible grille
            for xoff in range(N-sz+1):  # pour chaque position en x de la possible grille
#                print xoff, yoff, sz
                if chesscheck(B, xoff, yoff, sz):
                    B=fill(B, xoff, yoff, sz, 2)
                    nbi=nbi+1
                        
        if(nbi):
            nb.append((sz, nbi));
    print len(nb)
    for i in nb:
        print "{0} {1}".format(i[0], i[1])
