#! /usr/bin/python3

def readint():
    return int(input())
def readarray(f):
    return map(f, input().split())

_cases = readint()
for _case in range(_cases):
    (r,c) = readarray(int)
    grid = []
    for _ in range(r):
        grid.append(input())
    
    tgrid = list(map(lambda x: "".join(x), zip(*grid)))
    
    t = 0
    tt = ""
    
    for line in grid:
        first = 0
        while first < c and line[first] == '.':
            first += 1
        if first != c and line[first] == "<":
            if len(line.strip(".")) == 1 and len(tgrid[first].strip(".")) == 1:
                tt = "IMPOSSIBLE"
            else:
                t += 1
        last = c-1
        while last >= 0 and line[last] == '.':
            last -= 1
        if last != -1 and line[last] == ">":
            if len(line.strip(".")) == 1 and len(tgrid[last].strip(".")) == 1:
                tt = "IMPOSSIBLE"
            else:
                t += 1
        
    for line in tgrid:
        first = 0
        while first < r and line[first] == '.':
            first += 1
        if first != r and line[first] == "^":
            if len(line.strip(".")) == 1 and len(grid[first].strip(".")) == 1:
                tt = "IMPOSSIBLE"
            else:
                t += 1
        last = r-1
        while last >= 0 and line[last] == '.':
            last -= 1
        if last != -1 and line[last] == "v":
            if len(line.strip(".")) == 1 and len(grid[last].strip(".")) == 1:
                tt = "IMPOSSIBLE"
            else:
                t += 1
        
    if tt:
        print("Case #" + str(_case+1) + ":", tt)
    else:
        print("Case #" + str(_case+1) + ":", t)

