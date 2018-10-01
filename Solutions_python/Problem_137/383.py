import itertools
import sys
class board:
    def __init__(self,r,c,m):
        self.rows = r
        self.cols = c
        self.mines = m
        self.cells = []
        for x in range(r):
            self.cells.append([])
            
        for x in range(r):
            for y in range(c):
                self.cells[x].append([])

        for x in range(r):
                for y in range(c):
                    self.cells[x][y] = "."    
                    
            
    def copyBoard(self):
        newBoard = board(self.rows,self.cols,self.mines)
        for x in range(self.rows):
            for y in range(self.cols):
                newBoard.cells[x][y] = self.cells[x][y]
        return newBoard
    
    def lineartraversal(self):
        order = []
        for x in range(self.rows):
            for y in range(self.cols):
                order.append((x,y))
        return order
        
    def spiraltraversal(self):
        order = []
        center_x = self.rows/2 -1
        center_y = self.cols/2 -1
        order.append((center_x,center_y))
        radius = 1
        while ((len(order)) != (self.rows*self.cols)) and (radius <= max([self.rows,self.cols])):
            order.extend(self.getnthCircle(center_x,center_y,n=radius))
            radius += 1
            
        return order

    def getAllConfig(self):
            return itertools.combinations(self.lineartraversal(),self.mines)

    def applyConfig(self,config):
            for posn in config:
                x,y = posn
                self.cells[x][y] = "*"
            
    def getnthCircle(self,x,y,n=1):
        neighbours = []
        
        for t in range(-(n-1),n+1):    
            if ((x - n) >= 0) and ((y + t) < self.cols) and ((y+t) >= 0):
                neighbours.append((x-n,y+t))
        
        for t in range(-(n-1),n):    
            if ((x + t) < self.rows) and ((y+n)< self.cols) and ((x+t) >=0):
                neighbours.append((x+t,y + n))
                
        for t in range(n,-n-1,-1):    
            if ((x + n) < self.rows) and ((y + t) < self.cols) and ((y+t) >=0):
                neighbours.append((x+n,y+t))

        for t in range(n-1,-n-1,-1):
            if ((x + t) >= 0) and ((y-n) >= 0) and ((x+t) < self.rows):
                neighbours.append((x+t,y-n))
                                    
        return neighbours


    def showBoard(self):
        for x in range(self.rows):
                print ''.join(self.cells[x])

    def countMines(self,x,y):
        count = 0
        for t in self.getnthCircle(x,y,n=1):
            tx,ty = t
            if self.cells[tx][ty] == "*":
                count += 1
        return count              

    def countDots(self):
        count = 0
        for tx in range(self.rows):
            for ty in range(self.cols):
                if self.cells[tx][ty] == ".":
                    count += 1
        return count              
    
    def click(self,x,y):
        processing = []
        processed = set([])
        processing.append((x,y))
        while len(processing)>0:
            nx,ny = processing.pop(0)
            processed.add((nx,ny))
            mines = self.countMines(nx,ny)
            self.cells[nx][ny] = str(mines)
            if mines == 0:
                new = self.getnthCircle(nx,ny,n=1)
                processing.extend(filter(lambda(t): (t not in processed) and (t not in processing),new))
                
        return (self.countDots() == 0)
    
    def clearBoard(self):
        for tx in range(self.rows):
            for ty in range(self.cols):
                self.cells[tx][ty] = "."
                
    def play(self):
        for config in self.getAllConfig():
            self.clearBoard()
            self.applyConfig(config)
            for t in filter(lambda(z):(self.cells[z[0]][z[1]] == "."),self.lineartraversal()):
                tx,ty = t
                self.clearBoard()
                self.applyConfig(config)
                if self.click(tx,ty):
                    self.clearBoard()
                    self.applyConfig(config)
                    self.cells[tx][ty] = "c"
                    self.showBoard()
                    return True
        return False
        
file = open(sys.argv[1],"r")
n = int(file.readline())
for case in range(n):
    r,c,m = map(int,file.readline().split())
    b=board(r,c,m)
    print "Case #"+str(case+1)+":"
    if not b.play():
        print "Impossible"
        
        
