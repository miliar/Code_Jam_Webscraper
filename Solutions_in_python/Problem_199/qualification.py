filename = input("input file name: ")

def calculateFlips(S, K):
    flips = 0
    S = list(S)
    for i in range(len(S)):
        if(S[i]=="-"):

            if(i+K>len(S)):
                return -1
            else:
                print(S)
                for j in range(i, i+K):
                    if(S[j] == "-"):
                        S[j] = "+"
                    else:
                        S[j] = "-"
                flips+=1
    return flips

outputArray=[]
with open(filename, "r") as f:
    filearr = f.readlines()
    tests = int(filearr[0])
    for test in range(tests):
        currentTest = filearr[test+1]
        K = int(currentTest[currentTest.index(" ")+1:len(currentTest)])
        S = currentTest[0:currentTest.index(" ")]
        outputArray.append((test+1,calculateFlips(S,K)))

with open("out"+filename, 'w') as f:
    for t in outputArray:
        if (t[1] == -1):
            f.write("Case #%i: %s" % (t[0], "IMPOSSIBLE"))
        else:
            f.write("Case #%i: %i" % (t[0], t[1]))
        f.write("\n")