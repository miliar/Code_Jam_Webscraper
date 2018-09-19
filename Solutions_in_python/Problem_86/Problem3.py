'''
Created on 22.05.2011

@author: LordB
'''

inFile = open('C-small-attempt0.in', 'r')
outFile = open('output_Problem_3_small.txt', 'w')

nrOfCases = int( inFile.readline() )


for caseNr in range(1, nrOfCases+1):
    #print('Working on #', caseNr)
    
    tmp = inFile.readline().replace('\n','').split(" ")
    nrOfPlayers = int(tmp[0])
    lowest = int(tmp[1])
    heighest = int(tmp[2])
    
    
    freqs = inFile.readline().replace('\n','').split(" ")
    for f in freqs:
        f = int(f)
    
    found = False
    result = 0
    
    for i in range(lowest, heighest+1):
        found = True
        for f in freqs:
            f = int(f)
            if(i%f != 0 and f%i != 0): found = False
        if(found):
            result = i
            break
        
    if(result == 0): result = 'NO'
        
    print('Case #{}: {}'.format(caseNr, result))
    outFile.write('Case #{}: {}\n'.format(caseNr, result))