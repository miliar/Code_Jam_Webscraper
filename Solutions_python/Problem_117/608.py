'''
Created on Apr 13, 2013

@author: Nicolai Ommer <nicolai.ommer@gmail.com>
'''
import threading
# import threadpool
from multiprocessing import Process, Value, Array
# pool_sema = threading.BoundedSemaphore(value=8)

class Dimension:
    m = 0
    n = 0
    
    def __str__(self):
        return str(self.n) + "," + str(self.m)

def parseNM(strLine):
    mn = strLine.split(" ")
    dim = Dimension();
    dim.n = int(mn[0])
    dim.m = int(mn[1])
    return dim

class Executer(threading.Thread):
    lawns = []
    ident = -1
    def __init__(self, ident):
        threading.Thread.__init__(self)
        self.ident = ident
        self.lawns = list()
    
    def addLawn(self, lawn):
        self.lawns.append(lawn)
        
    def run(self):
        for lawn in self.lawns:
            print(lawn.ident)
            lawn.result.value = int(lawn.solve())
            print(str(lawn.ident) + " is done")
#             pool_sema.release()

class Lawn:
    ident = 0
    lawnPattern = None
    dim = None
    heights = None
    result = Value('b', False)
    
    def __init__(self, ident, dim, lawn):
        self.ident = ident
        self.dim = dim
        self.lawnPattern = lawn
        
    def heightSorted(self, rev):
        lheights = list()
        for rows in self.lawnPattern:
            for cell in rows:
                lheights.append(cell)
        return sorted(set(lheights), reverse=rev)
             
    def copyLawn(self, lawn):
        nLawn = list()
        for row in lawn:
            nLawn.append(list(row))
        return nLawn
             
    def mow(self, x,y,horizontal, lawn, h):       
        if horizontal:
            cy = y
            for cx in range(0, self.dim.m):
                if lawn[cy][cx] > h and self.lawnPattern[cy][cx] > h:
                    return False
            for cx in range(0, self.dim.m):
                lawn[cy][cx] = h
            return True
        else:
            cx = x
            for cy in range(0, self.dim.n):
                if lawn[cy][cx] > h and self.lawnPattern[cy][cx] > h:
                    return False
            for cy in range(0, self.dim.n):
                lawn[cy][cx] = h
            return True 
    
    def mowLawn(self, lawn, hi, x, y):
        while True:
            if x >= self.dim.m:
                x = 0;
                y += 1;
            if y >= self.dim.n:
                y = 0;
                if hi + 1 >= len(self.heights):
                    return True
                else:
                    hi +=1
            h = self.heights[hi]
                
            if self.lawnPattern[y][x] == h:
                if lawn[y][x] != h:
                    lawnbak = self.copyLawn(lawn)
                    if self.mow(x, y, True, lawn, h):
#                         print(lawn)
                        if self.mowLawn(lawn, hi, x+1, y):
                            return True
                        else:
                            lawn = lawnbak
                    if self.mow(x, y, False, lawn, h):
#                         print(lawn)
                        return self.mowLawn(lawn, hi, x+1, y)
                    else:
                        return False
            
            x += 1
                            
    def solve(self):
        lawn = list()
        for _ in range(self.dim.n):
            row = []
            for _ in range(self.dim.m):
                row.append(0)
            lawn.append(row)
        
        self.heights = self.heightSorted(rev=True)
        
        result = self.mowLawn(lawn, 0, 0, 0)
        return result
    
    def checkRowCol(self, x, y, h):
        cy = y
        for cx in range(0, self.dim.m):
            if self.lawnPattern[cy][cx] > h:
                break
        else:
            return True
            
        cx = x
        for cy in range(0, self.dim.n):
            if self.lawnPattern[cy][cx] > h:
                break
        else:
            return True
        return False
        
    def solve2(self):
        self.heights = self.heightSorted(rev=False)
        
        for h in self.heights:
            for y in range(0,self.dim.n):
                for x in range(0,self.dim.m):
                    if self.lawnPattern[y][x] == h:
                        if not self.checkRowCol(x,y,h):
                            return False
        return True


def doSolve(lawn, results):
#     print("solving " + str(lawn.ident))
    results[lawn.ident] = lawn.solve2()
#     lawn.result.value = results[lawn.ident]

if __name__ == '__main__':
    from datetime import datetime
    starttime = datetime.now()
#     f = open('../B-small-attempt0.in', 'r')
    f = open('../B-large.in', 'r')
#     f = open('../input.in', 'r')
    content = f.read()
    lines = content.splitlines()
    numCases = int(lines[0])
    lawns = []
#     print("Cases: " + str(numCases))
    
    lineNum = 1
    for case in range(numCases):
        dim = parseNM(lines[lineNum])
        lawn = []
        for n in range(dim.n):
            lineNum += 1
            lawn.append(map(int, lines[lineNum].split(" ")))
        lawns.append(Lawn(case, dim, lawn))
        lineNum += 1
    
#     pool = threadpool.ThreadPool(8)
#     requests = threadpool.makeRequests(doSolve, lawns)
#     for req in requests:
#         pool.putRequest(req)
#     pool.wait()
    
#     execs = []
#     for i in range(0,8):
#         execs.append(Executer(i))
#     
#     for lawn in lawns:
# #         pool_sema.acquire()
#         e = lawn.ident%8
#         execs[e].addLawn(lawn)
#     
#     for i in range(0,1):
#         execs[i].start()
#        
#     print("submitted")

    ps = list()
    results = Array('i', range(len(lawns)))
    for lawn in lawns:
        p = Process(target=doSolve, args=(lawn,results,))
        p.start()
        ps.append(p)
        
    for p in ps:
        p.join()    
       
    i = 1
#     for lawn in lawns:
    for result in results:
#         lawn.join()
#         print(lawn.result.value)
#         result = lawn.result.value
#         result = lawn.solve2()
        if result == 1:
            print("Case #" + str(i) + ": YES")
        else:
            print("Case #" + str(i) + ": NO")
        i += 1
    
    print(datetime.now() - starttime)