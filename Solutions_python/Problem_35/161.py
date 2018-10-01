#!/usr/bin/env python
import sys

EXTRA_HEIGHT = 10000 + 1
letters = 'abcdefghijklmnopqrstuvwxyz'
VOID_LETTER = ' '

f = open('input2.txt')

T = int(f.readline())

for mapIndex in range(1, T+1):
    
    map = []
    
    (H, W) = [int(t) for t in f.readline().split(' ')]
    
    for row in range(H):
        map.append( [[int(t), VOID_LETTER] for t in f.readline().split(' ')] )
    
    letterIndex = 0
    
    for h in range(H):
        for w in range(W):
            nhood = [] #plain ordered sequence of neighbours
            if h-1 >= 0: #North
                nhood.append((map[h-1][w][0], h-1, w))
            else:
                nhood.append((EXTRA_HEIGHT, 0, 0))
            if w-1 >= 0: #West
                nhood.append((map[h][w-1][0], h, w-1))
            else:
                nhood.append((EXTRA_HEIGHT, 0, 0))
            if w+1 < W: #East
                nhood.append((map[h][w+1][0], h, w+1))
            else:
                nhood.append((EXTRA_HEIGHT, 0, 0))
            if h+1 < H: #South
                nhood.append((map[h+1][w][0], h+1, w))
            else:
                nhood.append((EXTRA_HEIGHT, 0, 0))
            
            minAlt = (EXTRA_HEIGHT, 0, 0)
            
            #now we have N-W-E-S order and...
            for alt in (nhood):   #...in case of tie the first min cell will be chosen and it will be right 
                if alt[0] < minAlt[0]: #strict comparison
                    minAlt = alt
            
            if map[h][w][0] > minAlt[0]:  #slope case
                if map[h][w][1] == VOID_LETTER:
                    if map[minAlt[1]][minAlt[2]][1] == VOID_LETTER:
                        #get new letter for both
                        map[minAlt[1]][minAlt[2]][1] = letterIndex
                        map[h][w][1] = letterIndex
                        letterIndex+=1
                    else:
                        #simply get letter from minimal
                        map[h][w][1] = map[minAlt[1]][minAlt[2]][1]
                else: #slope has a letter           
                    if map[minAlt[1]][minAlt[2]][1] == VOID_LETTER:
                        #minimal neighbour gauraneed to be in current cell basin (according to waterfall moved down)
                        map[minAlt[1]][minAlt[2]][1] = map[h][w][1]
                    else: #both have letters
                        #if minimal neighbour has letter than it should replace all current letter occurences
                        minNbLetter = map[minAlt[1]][minAlt[2]][1]
                        curCellLetter = map[h][w][1]
                        #merge basin parts
                        for hh in range(H):
                            for ww in range (W):
                                if map[hh][ww][1] == curCellLetter:
                                    map[hh][ww][1] = minNbLetter
            else:
                #sink case: if we woudn't got here from another cell then it must be with a letter
                if map[h][w][1] == VOID_LETTER:
                    map[h][w][1] = letterIndex
                    letterIndex+=1


    #end for over entire map altitudes
    
    #now we should achieve lex. order
    passedLetters = {}
    
    letterIndex = 0

    for h in range(H):
        for w in range(W):
            if map[h][w][1] not in passedLetters:
                passedLetters[map[h][w][1]] = letters[letterIndex]
                map[h][w][1] = letters[letterIndex]
                letterIndex+=1
            else:
                map[h][w][1] = passedLetters[map[h][w][1]]
                
    #print
    print 'Case #' + str(mapIndex) + ':' 
    for h in range(H):
        s = ''
        for w in range(W):
            s += map[h][w][1] + ' '
        print s

f.close()
            
            












