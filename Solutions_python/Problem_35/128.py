# Uses pygraph, freely available from PyPI
import pygraph
from pygraph.algorithms.accessibility import connected_components

import psyco
psyco.full()

letters = "abcdefghijklmnopqrstuvwxyz"

def parseInput(f):
    lines = open(f).readlines()
    num_maps = int(lines[0])
    i = 1
    maps = []
    for m in range(num_maps):
        height, width = [int(x) for x in lines[i].split()]
        map = []
        i = i + 1
        for k in range(height):
            map.append([int(x) for x in lines[i].split()])
            i = i+1
        maps.append(map)

    return maps

def colorMap(m):
    g = pygraph.graph()
    height = len(m)
    width = len(m[0])
    
    for i in range(height):
        g.add_nodes([(i,x) for x in range(width)])
    
    for i in range(height):
        for j in range(width):
            candidates = []
            if i != 0:
                candidates.append((i-1, j))
            if j != 0:
                candidates.append((i, j-1))
            if j != width - 1:                
                candidates.append((i, j+1))
            if i != height - 1: 
                candidates.append((i+1, j))
            
            # find the best candidate and add the edge
            # to the graph
            val = m[i][j]
            if len(candidates) == 0:
                continue
            best_candidate = candidates[0]
            best_fall = val - m[best_candidate[0]][best_candidate[1]]

            for k in range(1, len(candidates)):
                new_candidate = candidates[k]
                new_fall = val - m[new_candidate[0]][new_candidate[1]]
                if new_fall > best_fall:
                    best_fall = new_fall
                    best_candidate = new_candidate
           
            if best_fall > 0: 
                g.add_edge((i,j), best_candidate)           
 
    return connected_components(g)

def getBasins(m):
    height = len(m)
    width = len(m[0])

    ret_m = []
    for i in range(height):
        ret_m.append([None] * width)

    current_letter = 0
    map = {}

    ccomps = colorMap(m)
    for i in range(height):
        for j in range(width):
            comp = ccomps[(i,j)]
            if comp in map:
                ret_m[i][j] = map[comp]
            else:
                map[comp] = letters[current_letter]
                current_letter += 1
                ret_m[i][j] = map[comp]
    
    return ret_m

if __name__ == '__main__':
    maps = parseInput('input.txt')
    i = 1
    for m in maps:
        print "Case #%s:" % i
        #for l in m:
        #    print " ".join([str(x) for x in l])
        #print
        for l in getBasins(m):
            print ' '.join(l)
        i = i + 1
