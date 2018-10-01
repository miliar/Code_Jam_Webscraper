'''
Created on 12 Apr 2014

@author: rich
'''

def magicTrick(pathin,pathout):
    # first line is t
    
    fi = open(pathin,"r")
    fo = open(pathout,"w")
    
    t = int(fi.readline())
    
    for i in range(t):
        x1 = int(fi.readline()) 
        
        row1 = []        
        for j in range(4):
            s = fi.readline()
            if (j+1) == x1:
                row1 = (int(x) for x in s.split(' '))
            
        x2 = int(fi.readline())
        row2 = []
        for j in range(4):
            s = fi.readline()
            if (j+1) == x2:
                row2 = (int(x) for x in s.split(' '))
        
        x = list(set(row1) & set(row2))
        
        result = "Case #" + str(i+1) + ": "
        
        n = len(x)
        if n == 0:
            result += "Volunteer cheated!"
        elif n > 1:
            result += "Bad magician!"
        elif n == 1:
            result += str(x[0])
        
        result += "\n"
        fo.write(result)

def cookieClicker(pathin,pathout):
    
    fi = open(pathin,"r")
    fo = open(pathout,"w")
    
    t = int(fi.readline())
    
    data = []
    for i in range(t):
        s = fi.readline()
        data = list((float(x) for x in s.split(' ')))
        
        C = data[0]
        F = data[1]
        X = data[2]
        
        cumt = 0. # total time
        y = 2.0 # coookie production
        
        while X/y > C/y + X/(y+F):
            cumt += C/y
            y += F
        
        cumt += X/y
        
        result = "Case #" + str(i+1) + ": " + '{0:.7f}'.format(cumt) + "\n"
        fo.write(result)
    
if __name__ == '__main__':
    
    cookieClicker("c:/rich_work/codejam2014/B-large.in","c:/rich_work/codejam2014/cookielarge.op")
    