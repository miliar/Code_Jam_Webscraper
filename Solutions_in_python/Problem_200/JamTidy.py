import JamFiles as Files

def check(num):
    #num = str(num)
    maxsofar = 0
    for x in num:
        if int(x) < maxsofar:
            return False
        else:
            maxsofar = int(x)
    return True

def dec(num, i):
    num[i] = "9"
    num[i-1] = str(int(num[i-1])-1)
    return num

def iterate(N):
    num = [x for x in str(N)]
    while not check(num):
        maxsofar = 0
        j = -1
        for i in range(0, len(num)):
            if int(num[i]) >= maxsofar:
                maxsofar = int(num[i])
            else:
                j = i
        if j != -1:
            print ("before: " , num)
            num = dec(num, j)
            print ("after: " , num)
    return int("".join(num))

def iterate2(N):
    maxsofar = 0
    for x in range(0,N+1):
        if check(str(x)):
            maxsofar = x
    return maxsofar

def iterate3(N):
    num = [x for x in str(N)]
    while not check(num):
        maxsofar = 0
        j = -1
        for i in range(0,len(num)):
            if num[i] != "9":
                j = i
        if j != -1:
            num = dec(num,j)
    return int("".join(num))



contents = Files.readInts("t2.in")[1:]
ans2 = []
ans3 = []

for N in contents:
    #ans2.append(iterate2(N))
    ans3.append(iterate3(N))
    
Files.writeFile(ans3, Files.syntax, "OutTidy.txt")
