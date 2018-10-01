import sys


class Language:
    BASECHAR=ord('a')

    def __init__(self):
        self.dictionary=[]
        pass

    def bitsFromChar(self,c):
        r=1<<(ord(c)-self.BASECHAR)
        return r

    def charsFromBits(self,bits):
        bit=1
        chars=""
        for i in range(26):
            if bit&bits:
                chars+=chr(i+self.BASECHAR)
            bit<<=1
        if len(chars)>1:
            chars="("+chars+")"
        return chars

    def parseWord(self,word):
        bitArray=[self.bitsFromChar(c) for c in word]
        return bitArray

    def parseFuzzyWord(self,word):
        multiSelect=False
        bitArray=[]
        elem=0
        for c in word:
            if c=="(":
                multiSelect=True
            elif c==")":
                multiSelect=False
            else:
                elem|=self.bitsFromChar(c)
            if not multiSelect:
                bitArray.append(elem)
                elem=0
        if elem:
            bitArray.append(elem)
        return bitArray

    def matchWords(self,word1,word2):
        for i in range(len(word1)):
            if not (word1[i]&word2[i]):
                return False
        return True

    def decode(self,bitArray):
        return "{ %r = %s }"%(bitArray,"".join([self.charsFromBits(b) for b in bitArray]))

    def learn(self,word):
        self.dictionary.append(word)

    def countMatches(self,fuzzyWord):
        n=0
        for word in self.dictionary:
            if self.matchWords(word,fuzzyWord):
                n+=1
        return n

language=Language()


input=open("A-large.in","r")
dimension=input.readline().strip().split()
(L,D,N)=(int(dimension[0]),int(dimension[1]),int(dimension[2]))

for i in range(D):
    word=language.parseWord(input.readline()[:L])
    language.learn(word)
    #print "word #%d = %r"%(i,language.decode(word))
    
output=open("A-large.out","w")
for i in range(1,N+1):
    testCase=language.parseFuzzyWord(input.readline().strip())
    #print "Case #%d: %d %s"%(i,language.countMatches(testCase),language.decode(testCase))
    output.write("Case #%d: %d\n"%(i,language.countMatches(testCase)))

input.close()
output.close()