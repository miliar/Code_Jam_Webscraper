'''
Created on 2010/05/22

@author: banana
'''

if __name__ == '__main__':
    pass

fp = open("1A-large.in", "r")

line = fp.readline()

T = int(line)

fpout = open("1A-large.txt", "w")

for t in range(1, T+1):
    line = fp.readline()
    N = int(line.split()[0])
    K = int(line.split()[1])
    field = [ [] for x in range(N)]
    for i in xrange(N):
        field[i] = fp.readline().rstrip()
        
    #print field

    for i in xrange(N):
        startpos = -1 
        dc = 0
        for j in xrange(N):
            if field[i][j] == "R" or field[i][j] == "B":
                startpos = j
                break   
        if startpos >= 0:
            dc = field[i][startpos:N].count(".")
            field[i] = field[i][0:startpos] + field[i][startpos:N].replace(".", "")
            field[i] = "." * dc + field[i]
           
                 
    #for l in field:
    #    print l
    
    found = { "R" : 0, "B" : 0}
    
    # yoko
    for i in xrange(N):
        for j in xrange(N-K+1):
            ch = field[i][j]
            if ch == ".":
                continue
            fail = 0
            for k in xrange(1, K):
                if j+k >= N or field[i][j+k] != ch:
                    fail = 1
                    break
            if fail == 0:
                found[ch] = 1
    
    # tate
    for i in xrange(N):
        for j in xrange(N-K+1):
            ch = field[j][i]
            if ch == ".":
                continue
            fail = 0
            for k in xrange(1, K):
                if j+k >= N or field[j+k][i] != ch:
                    fail = 1
                    break
            if fail == 0:
                found[ch] = 1
    
    # diag1
    for i in xrange(N-K+1):
        for j in xrange(N-K+1):
            ch = field[i][j]
            if ch == ".":
                continue
            fail = 0
            for k in xrange(1, K):
                if j+k >= N or i+k >= N or field[i+k][j+k] != ch:
                    fail = 1
                    break
            if fail == 0:
                found[ch] = 1
    
    # diag2
    for i in xrange(N-K+1):
        for j in xrange(N):
            ch = field[i][j]
            if ch == ".":
                continue
            fail = 0
            for k in xrange(1, K):
                if j-k < 0 or i+k >= N or field[i+k][j-k] != ch:
                    fail = 1
                    break
            if fail == 0:
                found[ch] = 1
    
    fpout.write("Case #%d: "%(t))
    
    if found["R"] == 1:
        if found["B"] == 1:
            fpout.write("Both\n")
        else:
            fpout.write("Red\n")
    else:
        if found["B"] == 1:
            fpout.write("Blue\n")
        else:
            fpout.write("Neither\n")
            
            
                 
        
            