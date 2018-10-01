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
    v = inFile.readline().replace("\n","").replace("\n","").split(" ")
    cLen = int(v[0])
    combine = v[1:cLen+1]
    oLen = int(v[cLen+1])
    opposed = v[cLen+2:cLen+2 + oLen]
    s = v[cLen+2 + oLen+1]
    return combine, opposed, s

#resolve testCase
def resolve(data):
    combine = data[0]
    opposed = data[1]
    s = data[2]
    hCombine = {}
    hOpposed = {}
    
    for i in xrange(len(combine)):
#        print combine[i][0:2]
#        print combine[i][0:2][::-1]
        hCombine[combine[i][0:2]] = combine[i][2];
        hCombine[combine[i][0:2][::-1]] = combine[i][2];        
    for i in xrange(len(opposed)):
        hOpposed[opposed[i]] = 1;
        hOpposed[opposed[i][::-1]] = 1;        
#    print hCombine, hOpposed
#    print s
    i=1;
    while 1:
        if i >= len(s):
            break
        if s[i-1:i+1] in hCombine.keys():
            s = s[0:i-1] + hCombine[s[i-1:i+1]] + s[i+1:]
            i = i - 1;
        else:
            for j in xrange(i):
                if (s[j] + s[i]) in hOpposed.keys(): 
                    s = s[i+1:]                    
                    i=0
                    break
        i = i + 1
    return str(list(s)).replace("'","").replace('"',"");


for i in range(nrOfTestCases):
    print "resolving testCase " + str(i + 1)
    out = resolve(readTestCase())
    outFile.writelines("Case #" + str(i + 1)+": " + str(out) + "\n")
outFile.close()


    
        