
import re, sys



def array(h,w):
    map =[] 
    for i in range(h):
        map += [[-1]*w]
    return map

def get_map(string, h, w):
    string = string.strip("\n")
    a = string.split("\n")
    map = []
    for i in range(len(a)):
        map += [a[i].split(" ")]
    
    for i in range(h):
        for j in range(w):
            map[i][j] = [int(map[i][j]), None]
    return map




pri = [(-1,0),(0,-1),(0,1),(1,0)]
def is_sink(map, i, j, h, w):
    for d in pri:
        ic = i + d[0]
        jc = j + d[1]
        if ic < 0 or jc < 0 or ic >= h or jc >= w: 
            continue
        if map[i][j][0] > map[ic][jc][0]:
            return False
    return True

def get_flow_cell_indexs(map, i, j, h, w):
    max_sa = -1
    ini=-1
    inj = -1
    
    for d in pri:
        ic = i + d[0]
        jc = j + d[1]
        if ic < 0 or jc < 0 or ic >= h or jc >= w: 
            continue
        sa = map[i][j][0] - map[ic][jc][0]
        if max_sa < sa:
            max_sa = sa
            ini,inj = ic,jc
    return ini,inj

labels = [chr(122 - x) for x in range(26)]
def get_label(map, i, j, h ,w):
    if not map[i][j][1] == None:
        return map[i][j][1]
    if is_sink(map, i, j, h, w):
        map[i][j][1] = labels.pop()
        return map[i][j][1]
    ni,nj = get_flow_cell_indexs(map, i, j, h, w)
    return get_label(map, ni, nj, h, w)
    
    
    
    

def get_dmap(map, h, w):
    for i in range(h):
        for j in range(w):
            map[i][j][1] = get_label(map, i, j ,h, w)
    #        print i,j,map[i][j][1]
    return map

def get_dmap_str(map, h,w):
    out=""
    for i in range(h):
        for j in range(w):
            out += map[i][j][1] + " "
        out = out.strip(" ") + "\n"
    return out

file = "./B-large"
fd = open(file + ".in","r")

param = fd.readline()
params = param.split(" ")
nump = int(params[0])

output = ""


case = "Case #No:"
no = 1

output = ""
for p in range(nump):
    labels = [chr(122 - x) for x in range(26)]
    param = fd.readline()
    params = param.split(" ")
    h = int(params[0])
    w = int(params[1])
    map_str = ""
    for i in range(h):
        map_str += fd.readline()
    map = get_map(map_str,h,w)
    map = get_dmap(map,h,w)
    dmap_str = get_dmap_str(map, h,w)
    c = case.replace("No", str(no))
    no += 1
    output += c + "\n"
    output += dmap_str

fd = open(file + ".out", "w")
fd.write(output)
fd.close
    

    