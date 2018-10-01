FILE_NAME = 'A-small-attempt0.txt'

cases = []
with open(FILE_NAME,'r') as file:
    x = file.readline()
    for line in file:
        word, e = line.split()
        cases.append((word,int(e)))



consonants = 'bcdfghjklmnpqrstvwxyz'

def generatesubstrings(string):
    for start in xrange(0,len(string)):
        for end in xrange(0,len(string)):
            yield string[start:end+1]

def check(word,x):
    count = 0
    for e in word:
        if count >= x:
            return True
        if e in consonants:
            count += 1
        else:
            count = 0
    return count >= x

def main(word,x):
    allcombos = generatesubstrings(word)
    total = 0
    for e in allcombos:
        if check(e,x):
            total += 1
    return total           

caseNum = 1        
with open('results.txt','w') as file:
    for e in cases:
        file.write('Case #{}: {}\n'.format(caseNum,main(e[0],e[1])))
        caseNum += 1
    
