fil=open('D:\\temp\\A-small-attempt1.in')

line=fil.readline()

def getData(line):
    '''To retrieve the integer from the data'''
    try:
        n=int(line[:line.index(' ')])
        line=line[line.index(' ')+1:]
    except ValueError:
        return int(line), line
    return n, line
L,line=getData(line)
D,line=getData(line)
N,line=getData(line)

dicLetters=[set() for i in xrange(L)]
dicList=[]

for i in xrange(D):
    line=fil.readline()[:-1]
    for j in xrange(L):
        dicLetters[j].add(line[j])
    dicList.append(line)

class WordList:
    '''To store the letters from a line'''
    def __init__(self, line):
        self.__letters=[]
        ind=0
        while ind<len(line):
            ch=line[ind]
            if ch=='\n':
                break
            elif ch=='(':
                pwd=''
                ind+=1
                while line[ind]!=')':
                    if line[ind] in dicLetters[len(self.__letters)]:
                        pwd+=line[ind]
                    ind+=1
                self.__letters.append(pwd)
            else:
                self.__letters.append(ch)
            ind+=1
    def hasWord(self, word):
        for i in xrange(L):
            if word[i] not in self.__letters[i]:
                return False
        return True

outFile=open('D:\\temp\\output.txt', 'w')
for i in xrange(N):
    line=fil.readline()
    wl=WordList(line)
    ctr=0
    for word in dicList:
        if wl.hasWord(word):
            ctr+=1
    print ctr
    outFile.write('Case #%s: %s\n'%(i+1, ctr))
outFile.close()
    
