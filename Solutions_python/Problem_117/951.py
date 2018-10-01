'''
Created on Apr 13, 2013

@author: ericdennison
'''


class Field(object):
    def __init__(self,a,b,f):
        # generate list[row][column]
        self.rows = [map(int,x.split()) for x in f]
        self.nrows = a
        self.ncols = b
        self.cols = [[r[i] for r in self.rows] for i in range(0,self.ncols)]
    
        
    
    def cellpossible(self,row,col):
        # possible if cell == max for either row or column
        return self.rows[row][col] in [max(self.rows[row]), max(self.cols[col])]
    
    def possible(self):
        for c in range(0,self.ncols):
            for r in range(0,self.nrows):
                if not self.cellpossible(r,c):
                    return "NO"
        return "YES"        

f = file("B-large.in").readlines()
fo = file("outputB.txt",'w')
ncases = int(f[0])

index = 1
for i in range(0,ncases):
    a,b = [int(x) for x in f[index].split()]
    jump = a+1
    fobj = Field(a,b,f[index+1:index+jump])
    fo.write("Case #{0}: {1}\n".format(i+1,fobj.possible()))
    index += jump