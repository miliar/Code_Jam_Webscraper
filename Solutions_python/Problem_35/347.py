import sys

filename = sys.argv[1]
#print "Using file", filename
input = open(filename, 'r')
outputname = filename[:-2] + "out"
output = open(outputname, 'w')

cases = int(input.readline())
#print cases, "test cases"
for case in range(1, cases + 1):
    output.write("Case #" + str(case) + ":\n")
    #print "Case", case
    
    H, W = (int(x) for x in input.readline().split())
    hmap = {}
    drainmap = {}
    for row in range(H):
        for col, val in enumerate(input.readline().split()):
            hmap[(col, row)] = int(val)
    
    #def printmap(m, h, w):
        #for y in range(h):
            #print ' '.join( str(m[x, y]) for x in range(w) )
    
    #printmap(hmap, H, W)
    
    letters = [chr(i) for i in xrange(ord('a'), ord('z')+1)]
    #print "letters:", letters
    global useletter
    useletter = 0
    
    def tobasin(x, y, w, h):
        #print (x, y)
        # N = 0, W = 1, E = 2, S = 3
        movetuples = { 0: (x, y - 1), 1: (x - 1, y), 2: (x + 1, y), 3: (x, y + 1) }        
        moveto = None
        val = None
        if y > 0:
            moveto = 0
            val = hmap[movetuples[0]]
        if x > 0 and (val == None or hmap[movetuples[1]] < val):
            moveto = 1
            val = hmap[movetuples[1]]
        if x < (w - 1) and (val == None or hmap[movetuples[2]] < val):
            moveto = 2
            val = hmap[movetuples[2]]
        if y < (h - 1) and (val == None or hmap[movetuples[3]] < val):
            moveto = 3
            val = hmap[movetuples[3]]
        if moveto == None:
            drainmap[(x, y)] = letters[useletter]
            return letters[useletter]
        if val >= hmap[(x, y)]: # sink
            color = None
            if (x, y) in drainmap.keys():
                color = drainmap[(x, y)]
            else:
                color = letters[useletter]
                global useletter
                useletter = useletter + 1
            drainmap[(x, y)] = color
            #print color
            return color
        else:
            nx, ny = movetuples[moveto]
            color = tobasin(nx, ny, w, h)
            #print (x, y), "=", color
            drainmap[(x, y)] = color
            return color
    
    for y in range(H):
        for x in range(W):    
            tobasin(x, y, W, H)
          
    #print drainmap  
    #printmap(drainmap, H, W)
    
    for y in range(H):
        output.write(' '.join( str(drainmap[x, y]) for x in range(W) ) + "\n")
    
input.close()
output.close()
