import pprint
import string

if __name__ == "__main__":
    fin  = open('d:\\b.in', 'r')
    fout = open('d:\\b.out', 'w')
    T = int(fin.readline())
    for i in range(1, T+1):
        print('Line %d' % i)
        line = fin.readline().split()
        H = int(line[0])
        W = int(line[1])       
        map = []
        for j in range(H):
            ar1 = fin.readline().split()
            ar2 = []
            for x in ar1:
                ar2.append(int(x))
            map.append(ar2)
        #pprint.pprint(map)
        rmap = [[['?', -1]for j in range(W)] for k in range(H)]
        #pprint.pprint(rmap)      
        basin = 0
        stack = [[0, 0]]
        rmap[0][0][0] = 'a'
        
        for y in range(H):
            for x in range(W):
                e = 0;
                if (y > 0):
                    if ((map[y][x] - map[y-1][x]) > e):
                        rmap[y][x][1] = 0;
                        e = map[y][x] - map[y-1][x];
                if (x > 0):
                    if (map[y][x] - map[y][x-1]) > e:
                        rmap[y][x][1] = 1;
                        e = map[y][x] - map[y][x-1];
                if (x < W-1):
                    if (map[y][x] - map[y][x+1]) > e:
                        rmap[y][x][1] = 2;
                        e = map[y][x] - map[y][x+1];
                if (y < H-1):
                    if (map[y][x] - map[y+1][x]) > e:
                        rmap[y][x][1] = 3;
                        e = map[y][x] - map[y+1][x];

        #pprint.pprint(rmap)
        
        def func():
            global H
            global W
            global map
            global rmap
            global basin
            global stack
            
            p = stack.pop()
            x = p[0]
            y = p[1]
            
            if rmap[y][x][1] == 0:
                rmap[y-1][x][0] = string.ascii_lowercase[basin]
                stack.append([x, y-1])
            elif rmap[y][x][1] == 1:
                rmap[y][x-1][0] = string.ascii_lowercase[basin]
                stack.append([x-1, y])
            elif rmap[y][x][1] == 2:
                rmap[y][x+1][0] = string.ascii_lowercase[basin]
                stack.append([x+1, y])
            elif rmap[y][x][1] == 3:
                rmap[y+1][x][0] = string.ascii_lowercase[basin]
                stack.append([x, y+1])
            
            if (y > 0):
                if rmap[y-1][x][0] == '?':
                    if rmap[y-1][x][1] == 3:
                        rmap[y-1][x][0] = string.ascii_lowercase[basin]
                        stack.append([x, y-1])
            if (x > 0):
                if rmap[y][x-1][0] == '?':
                    if rmap[y][x-1][1] == 2:
                        rmap[y][x-1][0] = string.ascii_lowercase[basin]
                        stack.append([x-1, y])
            if (x < W-1):
                if rmap[y][x+1][0] == '?':
                    if rmap[y][x+1][1] == 1:
                        rmap[y][x+1][0] = string.ascii_lowercase[basin]
                        stack.append([x+1, y])
            if (y < H-1):
                if rmap[y+1][x][0] == '?':
                    if rmap[y+1][x][1] == 0:
                        rmap[y+1][x][0] = string.ascii_lowercase[basin]
                        stack.append([x, y+1])
            
            if len(stack) == 0:
                for i in range(H):
                    for j in range(W):
                        if rmap[i][j][0] == '?':
                            stack.append([j, i])
                            basin += 1
                            rmap[i][j][0] = string.ascii_lowercase[basin]
                            return        
            return
        
        
        while len(stack) > 0: func()
        #pprint.pprint(rmap)
        
        fout.write('Case #%d:\n' % i)
        for y in range(H):
            for x in range(W):
                fout.write('%c ' % rmap[y][x][0])
            fout.write('\n')
    
    
    
    
    
    