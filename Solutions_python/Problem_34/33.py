'''
Created on Sep 3, 2009

Question A

@author: AliJ
'''

def tokenize_word(theWord):
    
    curPos = 0
    tokenized = []
    for i in range(wordLength):
        if theWord[curPos] == "(":
            endPos = theWord.find(")", curPos)
            tokenized.append(theWord[curPos+1:endPos])
            curPos=endPos+1
        else:
            tokenized.append(theWord[curPos])
            curPos+=1
            
    return tokenized
            

def compare(word, tokWord):
    
    for i in range(wordLength):
        if word[i] not in tokWord[i]:
            return False
    
    return True


def process_case():

    word = raw_input().strip()
    tokWord = tokenize_word(word)
    
    numMatches = 0
    
    for w in dict:
        if compare(w, tokWord):
            numMatches += 1
    
    return numMatches


(L,D, N) = raw_input().split()

numCases = int(N)
wordLength = int(L)
dictLength = int(D)

dict = []


for i in range(dictLength):
    dict.append(raw_input().strip())

for i in range(numCases):
            
    print "Case #"+str(i+1)+":", (process_case())
