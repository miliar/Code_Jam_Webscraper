class PermutationListGetter:
    def __init__(self,tokens):
        self.tokens=tokens
        self.permutationList=[]
    
    def getPermutationList(self):
        for token in self.tokens:
            if len(token)==1:
                self.addToTokenList(token)
            else:
                self.splitAndAdd(token)
        return self.permutationList
    
    def addToTokenList(self,token):
        if len(self.permutationList)==0:
            self.permutationList.append(token)
        else:
            for i in range(len(self.permutationList)):
                self.permutationList[i]+=token
    def splitAndAdd(self,token):
        tokens=list(token)
        if len(self.permutationList)==0:
            for permutation in tokens:
                self.permutationList.append(permutation)            
        else:
            newList=[]
            tokens=list(token)
            for suffix in tokens:
                for permutation in self.permutationList:
                    newList.append(permutation+suffix)
            self.permutationList=[]
            for permutation in newList:
                self.permutationList.append(permutation)
    