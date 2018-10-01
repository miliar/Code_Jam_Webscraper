infile = open('A-large.in','r')
outfile = open('output.txt', 'w')

class Node:
    # row, col, next
    pass

def find(grid, row, col, rdir, cdir, nodes):
   # print(row,col,rdir,cdir)
    row += rdir
    col += cdir
    #print(row,col)
    while row>=0 and row <len(grid) and col>=0 and col<len(grid[0]):
        if grid[row][col] != '.':
            #print(findnode(nodes,row,col))
            return findnode(nodes, row, col)
        row += rdir
        col += cdir
   # print("None")
    return None

def findnode(nodes, row, col):
    for node in nodes:
        if node.row == row and node.col == col:
            return node
    print("ERROR NOT FOUND")
    return None

T = int(infile.readline().strip())
out = ""
for tc in range(T):
    #print("TEST CASE",tc)
    out += "Case #"+str(tc+1)+": "
    
    R,C = infile.readline().split()
    R,C = (int(R),int(C))
    grid=[]
    for i in range(R):
        grid.append(infile.readline().strip())
    # now create nodes and link them
    
    nodes = []
    
    # find nodes
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ".":
                continue
            node = Node()
            node.row = row
            node.col = col
            node.pathnum = -1
            node.nextnode = None
            node.prevnode = None
            nodes.append(node)
    
    # hook up nodes
    for node in nodes:
        if grid[node.row][node.col] == "^":
            node.nextnode = find(grid,node.row,node.col,-1,0,nodes)
            if node.nextnode != None:
                node.nextnode.prevnode = node
            #print("NODE",node.row,node.col,node.nextnode,node.prevnode)
        elif grid[node.row][node.col] == "v":
            node.nextnode = find(grid,node.row,node.col,1,0,nodes)
            if node.nextnode != None:
                node.nextnode.prevnode = node
        elif grid[node.row][node.col] == "<":
            node.nextnode = find(grid,node.row,node.col,0,-1,nodes)
            if node.nextnode != None:
                node.nextnode.prevnode = node
        elif grid[node.row][node.col] == ">":
            node.nextnode = find(grid,node.row,node.col,0,1,nodes)
            if node.nextnode != None:
                node.nextnode.prevnode = node
        
    # find topnodes and singleton nodes
    topnodes = []
    singletons = []
    #print("NODES")
    for node in nodes:
        #print(node,node.row, node.col, node.nextnode, node.prevnode)
        if node.prevnode == None:
            if node.nextnode == None:
                singletons.append(node)
               # print(tc,"S",node.row,node.col)
            else:
                topnodes.append(node)
                #print(tc,"T",node.row,node.col)
    
    # follow each path
    nextpathnum = 1
    cycles = []
    for node in nodes:
        if node.pathnum == -1 and node not in singletons:
            pathnum = nextpathnum
            node.pathnum = pathnum
            current = node
            visited = [current]
            while current.nextnode != None:
                if current.nextnode.pathnum == pathnum:
                    # cycle. quit.
                    cycles.append(pathnum)
                    nextpathnum += 1
                    break
                elif current.nextnode.pathnum == -1:
                    current.nextnode.pathnum = pathnum
                    current = current.nextnode
                    visited.append(current)
                else:
                    # we joined another path
                    # renumber our path and quit
                    pathnum = current.nextnode.pathnum
                    for n in visited:
                        n.pathnum = pathnum
                    break
            if current.nextnode == None:
                nextpathnum += 1
    numpaths = nextpathnum-1
    # every non-cycle needs to be fixed
    fixes = numpaths - len(cycles) 
    #print(numpaths)
    #print(cycles)
    #print(singletons)
    
    # every singleton needs to connect to a path or to another singleton 
    fixedsingletons = []
    for node in singletons:
        if node not in fixedsingletons:
            found = [
                find(grid, node.row, node.col, 0, -1, nodes),
                find(grid, node.row, node.col, 0, 1, nodes),
                find(grid, node.row, node.col, -1, 0, nodes),
                find(grid, node.row, node.col, 1, 0, nodes),
                ]
            #print(found)
            singleton = None
            for f in found:
                if f != None:
                    if f.pathnum != -1:
                        fixes += 1
                        node.pathnum = f.pathnum
                        break
                    else:
                        singleton = f
            if node.pathnum == -1:
                if singleton == None:
                    fixes = -1
                    break
                node.pathnum = nextpathnum
                nextpathnum += 1
                singleton.pathnum = node.pathnum
                fixedsingletons.append(singleton)
                fixes += 2
    if fixes == -1:
        out += "IMPOSSIBLE"
    else:
        out += str(fixes)
    out += "\n"
    
print(out)
outfile.write(out)
    
outfile.close()
infile.close()