'''
Created on Apr 30, 2011

@author: Marius Dorin Moraru
'''

#filename without extension
#fileName = raw_input("Enter a name:")
fileName = "c:/learn/a"

inFile = open(fileName + ".in", "rU")
outFile = open(fileName + ".out", "w")

nrOfTestCases = long(inFile.readline());        
print "nrOfTestCases " + str(nrOfTestCases)









def readTestCase():   
    v = inFile.readline().replace("\n","").replace("\r","").split(" ")
    r = int(v[0])
    c = int(v[1])
    w =[]
    for i in xrange(r):
        w.append(list(inFile.readline().replace("\n","").replace("\r","")+"."))
    return r, c, w

#resolve testCase
def resolve(data):    
    r = data[0]
    c = data[1]
    w = data[2]
    
    s = "";
    while len(s) < c:
        s = "." + s;
    w.append(list(s))
#    print w
    
    for i in xrange(r):
        for j in xrange(c):
            if w[i][j] == "#":
                if w[i+1][j] == "#" and w[i][j+1] == "#" and w[i+1][j+1] == "#":
                    w[i][j] = "/";
                    w[i][j+1] = "\\";
                    w[i+1][j] = "\\";
                    w[i+1][j+1] = "/";
                else:
                    return "\nImpossible"; 
    
    s = ""
    for i in xrange(r):
        s = s + "\n"
        for j in xrange(c):
            s = s + w[i][j];
        
    
    return s







for i in range(nrOfTestCases):
    print "resolving testCase " + str(i + 1)
    out = resolve(readTestCase())
    outFile.writelines("Case #" + str(i + 1)+": " + str(out) + "\n")
outFile.close()


    
        