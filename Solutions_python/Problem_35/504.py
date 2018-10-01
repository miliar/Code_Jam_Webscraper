from __future__ import division

global cn
global alphabet

cn = 1
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def format(res):
    global cn
    print "Case #" +  str(cn) + ":\n", res
    cn += 1

import os
lines = open(os.getcwd() + '/' + "input.txt").read().split("\n")



def appendIfHigestYet(ar, x, y, score):
    if len(ar) == 0 : 
        ar.append([x, y, score])
        return ar
    if (ar[0][2] > score): return ar #no change needed
    if (ar[0][2] == score):
        ar.append([x, y, score])
        return ar #tie
    if (ar[0][2] < score): 
        ar =  [[x, y, score]] 
        return ar #score wins
    

def getNeighbors(x, y, arr):
    """returns array in the form [x, y]"""
    h = len(arr)-1
    w = len(arr[0])-1
    res = []
    
    #In case of a tie, water will choose the first direction with the lowest altitude from this list: North, West, East, South.
    
    
    if x > 0 and h+1 != 1: 
        res += [[x-1,y]] #NORTH
    
    if y > 0 and w+1 != 1: 
        res += [[x,y-1]] #WEST
    
    if y < w and w+1 != 1: 
        res += [[x,y+1]] #EAST
    
    if x < h and h+1 != 1: 
        res += [[x+1,y]] #SOUTH
    

    

    
    return res



def floodFill(arr, pos, heightmap):
    
    basin_char = arr[pos[0]][pos[1]]
    
    queue = [pos]
    
    h = len(arr)-1
    w = len(arr[0])-1


    arrcopy = [x[::] for x in arr]


    #how this algorithm should work
    
    # for each item in q
    #for each item that q touches
    # if touching item will flow into q
    #success! add touching into q and basin

    while len(queue) > 0:
        qVal = heightmap[queue[0][0]][queue[0][1]]
        
        for markoff in queue: arrcopy[markoff[0]][markoff[1]] = "D"
        
        #for each item that q touches
        for nei in getNeighbors(queue[0][0], queue[0][1], m):
            nVal = heightmap[nei[0]][nei[1]]
                                     
            if arrcopy[nei[0]][nei[1]] != "D":
                queue.append(nei)
                
            # if touching item would rather flow into q than anywhere else
            fastest = []
            for nei2 in getNeighbors(nei[0], nei[1], m):
                fastest = appendIfHigestYet(fastest, nei2[0], nei2[1],  nVal - m[nei2[0]][nei2[1]]  )
            
            
            
            for v in fastest:
                if v[2] <= 0: break
                if arr[v[0]][v[1]] == basin_char:
                    arr[nei[0]][nei[1]] = basin_char
                    break
                else :
                    break
            
        queue = queue[1:]

    return arr

important_nums = lines[0].split(" ")
lines = lines[1:]

while len(lines)>0:
    h = int(lines[0].split(" ")[0])
    lines = lines[1:]
    m = lines[:h]
    m = [[int(x) for x in line.split(' ')] for line in m]
    hconst = len(m)
    h = len(m)-1
    w = len(m[0])-1
    mcopy = [x[::] for x in m]
    
    bIndex = 0
    #label basins correctly
    basins = []
    
    #find, label basins
    for i, line in enumerate(m): #h
        for j, val in enumerate(line): #w
            higher = 0
            max = 0
            for nei in getNeighbors(i, j, m):
                max += 1
                if m[nei[0]][nei[1]] >= val:
                    higher += 1

            if higher == max: 
                mcopy[i][j] = alphabet[bIndex]
                basins.append([i, j])
                bIndex += 1
                

    for b in basins:
        mcopy = floodFill(mcopy, b, m)
    
    #almost there!
    
    
    inorder=[]
    hash = {}
    for i, line in enumerate(mcopy): 
        for j, val in enumerate(line): 
            if not mcopy[i][j] in hash:
                hash[mcopy[i][j]] = True
                inorder.append(mcopy[i][j])
    
    inorder = zip(inorder, alphabet)
    
    for item in inorder: #potentially BADDDDDDD
        for i, line in enumerate(mcopy): 
            for j, val in enumerate(line): 
                if mcopy[i][j] == item[0]: mcopy[i][j] = "$"+item[1]

    for i, line in enumerate(mcopy): 
        for j, val in enumerate(line): 
            mcopy[i][j] = mcopy[i][j][1:]
    
    prop = "\n".join([ " ".join(line) for line in mcopy])
    
    
    format( prop)

            
    # link basins together

    lines = lines[hconst:]