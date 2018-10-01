
numberMap = {"1":0,"i":1, "j":2, "k":3}

prodMat = [["1","i","j","k"],["i","-1","k", "-j"],["j","-k","-1","i"],["k","j","-i","-1"]]

def isCorrect(L,X,ans):
    if (L*X < 3):
        return "NO"
    res = "1"
    for z in range(min(4*L,X*L)):
        i = z % L
        res = quadProduct(res,ans[i])
        if res == "i":
            if(z == L*X - 2):
                
                return "NO"
            newRes = "1"
            for y in range(z+1, min(X*L, z+1+4*L )):
                j = y % L
                newRes = quadProduct(newRes,ans[j])
                if newRes == "j":                                  
                    if(y == L*X - 1):                       
                        return "NO"
                    last = "1"
                    for w in range(y+1, X*L):
                        k = w% L
                        last = quadProduct(last,ans[k])
                    if last == "k":
                        return "YES"
                    break
            break
    return "NO"
                
            

def quadProduct(x,y):
    if(x[0] == "-"):
        if not y[0] == "-":
            res = quadProduct(x[1],y)
            if res[0] == "-":
                return res[1]
            return "-" + res
        else:
            return quadProduct(x[1],y[1])       

    if(y[0] == "-"):
        if not x[0] == "-":
            res = quadProduct(x,y[1])
            if res[0] == "-":
                return res[1]
            return "-" + res
        else:
            return quadProduct(x[1],y[1])  
        
    x2 = numberMap[x]
    y2 = numberMap[y]
    return prodMat[x2][y2]


        
    

f = open("one.in", "r").read()

#new_file = open("sma.txt", "w")
splitted_file = f.split("\n")[:]

lineCounter =1
amountOfLines = len(splitted_file)

case = 0

while(lineCounter < amountOfLines):
    case += 1
    firstLine = splitted_file[lineCounter]
    lineCounter += 1

    secondLine = splitted_file[lineCounter]
    lineCounter+= 1
    
    L,X = firstLine.split(" ")
    L,X = [int(L), int(X)]
    ans = secondLine
    out = isCorrect(L,X,ans)
    print "Case "+ "#"+str(case) +": " + out
    
    
