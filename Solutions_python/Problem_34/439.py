f = open('A-large.in')

l,d,n = map(lambda x: int(x), f.readline().split())

words = []

def searchRange(headChar, wordlist):
    result = []
    
    for x in wordlist:
        if x[0] == headChar:
            result.append(x[1:])

    return result
    
def getMatched(keyword, rword):

    #print '-----'
    #print keyword
    #print rword

    rword.sort()
    
    if len(keyword) == 0:
        return len(rword)
    
    new_rword = []
    
    if keyword[0] == '(':
        idx = keyword.find(')')
        
        for x in keyword[1:idx]:
            new_rword.extend(searchRange(x, rword))
        
        return getMatched(keyword[idx+1:],new_rword)

    else:
        new_rword.extend(searchRange(keyword[0], rword))
        
        return getMatched(keyword[1:],new_rword)    

outf = open('result','w')

for x in range(d):
    words.append(f.readline().strip())

for x in range(n):
    outf.write ("Case #"+str(x+1)+": ")
    rword = f.readline().strip()

    outf.write(str(getMatched(rword, words)))
    outf.write('\n')

f.close()
outf.close()
