'''
Created on 14.04.2012

@author: Philip
'''

if __name__ == '__main__':
    pass

inputFile  = open('inputExample.txt', 'r')
outputFile = open('outputExample.txt', 'r')

nrInputCases = inputFile.readline()
nrInputCases = int(nrInputCases)
nrOutputCases = outputFile.readline()
nrOutputCases = int(nrOutputCases)

subDict = {'y' : 'a', 'e':'o', 'q':'z', 'z' : 'q'}
while nrInputCases > 0:
    nrInputCases -= 1
    lineCoded = inputFile.readline()
    lineOrg = outputFile.readline()
    
    for i in range(0,len(lineCoded)):
        sub = lineCoded[i] 
        if (sub != ' ') and (sub != '\n') and (sub != '\r'):
            org = lineOrg[i]
            if sub in subDict.keys():
                if subDict[sub] != org:
                    print "Error " + sub + " was previously identified as " + subDict[sub] + " is now said to be: " + org
            else:
                subDict[sub] = org
                     
print "subDict = {",
first = True
for key in sorted(subDict.keys()):
    if not(first):
        print ", ",
    print " '" + key + "' : '" + subDict[key]   + "'",
    first = False
print "}"
print str(sorted(subDict.keys()))
print str(sorted(subDict.values()))

inputFile.close()        
outputFile.close()     