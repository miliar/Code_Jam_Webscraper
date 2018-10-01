
def switch(c):
    if c == "+": 
        return "-"
    else: 
        return "+"
numberOfInputs = 0
out = open("output.txt", "w")

with open("A-large.in") as f:
    numberOfInputs = int(f.readline())
    for num in range(1,numberOfInputs +1):
        cakestr, k = f.readline().split(" ")
        k = int(k) 
        #print(cakestr, " .... ", k)
        moves = 0
        seen = set()
        while True:
            #print("str " , cakestr)
            if cakestr in seen:
                moves = "IMPOSSIBLE"
                break
            seen.add(cakestr)        
            cakes = list(cakestr)
            for i in range(len(cakes)-(k-1)):
                if cakes[i] == "+": continue
                cakes[i] = "+"
                for j in range(1,k):
                    cakes[i+j] = switch(cakes[i+j])
                moves +=1
            cakestr = ''.join(cakes)
            
            failed = False
            for c in cakestr:
                if c == "-":
                    failed = True
            if not failed:
                break
            
        #print("Case #{0}: {1}\n".format(num, moves))
        out.write("Case #{0}: {1}\n".format(num, moves))



out.close()
