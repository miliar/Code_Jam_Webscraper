f = open("A-large (1).in","r").readlines()
g = open("A-large.txt",'w')
testcases = int(f[0])
line_no = 1

for j in range(1,testcases+1):
    
    line = f[line_no].strip().split()
    r = int(line[0])
    c = int(line[1])
    print([r,c])
    
    grid = []
    for i in range(r):
        grid.append(list(f[line_no + i + 1].strip()))
     
    print(grid)
    reverse = False
    for row in range(r):
       
        todo = []
        boss_present = False
        for column in range(c):
            
            piece = grid[row][column]
            if piece != "?":
                boss_present = True
                boss = piece
                for items in todo:
                    grid[items[0]][items[1]] = boss
                todo.clear()
                    
            
            else:
                if boss_present:
                    grid[row][column] = boss
                
                else:
                    todo.append([row,column])
        
        if todo != []:
            if row == 0:
                reverse = True
            elif grid[row-1][0] != "?":
                for items in todo:
                    grid[items[0]][items[1]] = grid[items[0]-1][items[1]]
        print(grid)  
                    
    if reverse:
        for x in range(r-1, -1, -1):
            if grid[x][0] == "?":
                for y in range(c):
                    grid[x][y] = grid[x+1][y]
                    
    print(grid)
    line_no = line_no + r + 1
    g.write("Case #"+ str(j) + ":" +'\n')
    
    for z in range(r):
        out =""
        for q in range(c):
            out += grid[z][q]
            
        g.write(out + '\n')
        print(out)
            
        
                
        
            
            
            
    