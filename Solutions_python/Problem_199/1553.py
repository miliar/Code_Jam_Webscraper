import sys
sys.setrecursionlimit(1000000)

def flip(strpan, K, H):
    for i in range(H, H+K):
        if strpan[i] == "-":
            strpan[i] = "+"
        elif strpan[i] == "+":
            strpan[i] = "-"
    return strpan

def chkHFU(strpan):
    for ele in strpan:
        if ele != "+":
            return False
    return True

def fliprec(strpan, flipcount, K, H):
    global globFlipCount
    #print strpan
    
    if H + K > len(strpan):
        if chkHFU(strpan):
            globFlipCount = flipcount
        else:
            globFlipCount = -1
    else:
        if strpan[H] == "-":
            strpan = flip(strpan, K, H)
            fliprec(strpan, flipcount + 1, K, H + 1)
        else:
            fliprec(strpan, flipcount, K, H + 1)

globFlipCount = 0

def flipstart(strpan, K):
    global globFlipCount
    globFlipCount = 0 
    fliprec(list(strpan), 0, K, 0)
    if globFlipCount >= 0:
        return str(globFlipCount)
    return "Impossible"
            
f = open("A-large(4).in", "r")

T = int(f.readline())

for x in range(0, T):
    readline = f.readline().strip()
    pan, K = readline.split(" ")
    print "Case #" + str(x+1) + ": " + flipstart(pan, int(K))
        

'''
print flip(list("--+--"), 3, 1)
    
fliprec(list("---+-++-"), 0, 3, 0)
fliprec(list("+++++"), 0, 4, 0)
fliprec(list("-+-+-"), 0, 4, 0)
'''