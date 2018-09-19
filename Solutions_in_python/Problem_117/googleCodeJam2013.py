import math

def checkCellBlocked():
    
    if table[j][i] == "1":
        
        blocked = False
        for k in range(N):
            if table[k][i] == "2":
                blocked = True
        if blocked:   
            for k in range(M):
                if table[j][k] == "2":
                    return True
    return False

# Qualification round
inp = open("input.txt")
outp = open("output.txt","w")

CASES = int(inp.readline())

for case in range(CASES):
    N,M = inp.readline().split()
    N,M = int(N),int(M)
    table = []
    result = "YES"
    for j in range(N):
        table.append(inp.readline().split())
        
    for j in range(N):
        for i in range(M):
            blocked = checkCellBlocked()
            if blocked:
                result = "NO"
                
            
    outp.write("Case #%s: %s\n" % (case+1,result))     
    #outp.write("Case #%s: %s\n" % (case+1,count)) 
    
           
inp.close()
outp.close()