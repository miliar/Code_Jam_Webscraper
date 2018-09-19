'''
Created on Sep 3, 2009

Question C

@author: AliJ
'''

def formatNum(i):
    i = i % 10000
    result = str(i)
    if i >= 1000:
        return result
    elif i >= 100:
        return "0"+result
    elif i >=10:
        return "00"+result
    else:
        return "000"+result
    

def process_case():
    thePhrase = "welcome to code jam"
    
    theLine = raw_input().strip()
    
    if len(theLine) == 0:
        return 0
    

    # Idea: counts[x][y] stores the number of occurences of thePhrase[0:y] as a subsequence in 
    # theLine[0:x]. 
    counts = [[0 for i in range(len(thePhrase)+1)] for j in range(len(theLine)+1)]
    
    for j in range(len(theLine)+1):
        counts[j][0] = 1
        
    for j in range(1, len(theLine)+1):
        for i in range(1, len(thePhrase)+1):
            counts[j][i] = counts[j-1][i]
            if theLine[j-1] == thePhrase[i-1]:
                counts[j][i] += counts[j-1][i-1] % 10000
            
    return formatNum(counts[len(theLine)][len(thePhrase)])



numCases = int(raw_input())

for i in range(numCases):
            
    print "Case #"+str(i+1)+":", (process_case())