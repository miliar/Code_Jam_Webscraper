from PermutationListGetter import PermutationListGetter
class PermutationFinder:
    def __init__(self,sequence,maxWordLength,dictionary):
        self.sequence=sequence
        self.maxWordLength=maxWordLength
        self.tokens=[]
        self.dictionary=dictionary
        
    def findPermutation(self):
        self.getTokens(self.sequence)
        plg=PermutationListGetter(self.tokens)
        return self.tokens
        
    def getTokens(self,sequence):
        end=0
        allTokens=sequence.split("(")
        for token in allTokens:
            if token.find(")")!=-1:
                subTokens=token.split(")")
                self.addSingleToken(subTokens[0])
                self.addMultipleToken(subTokens[1])
            else:
                self.addMultipleToken(token)
    
    def addSingleToken(self,token):
        self.tokens.append(list(token))
    
    def addMultipleToken(self,token):
        if token!='':
            characterList=list(token)
            for character in characterList:
                self.tokens.append(list(character))
    