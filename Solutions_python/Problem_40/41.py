import sys

ifs = file("input.txt")
ofs = file("output.txt", "w")

def ReadInts(input = ifs):
  return list(map(int, input.readline().strip().split(" ")))

def GetMatrix(rows, cols, value=0):
    return [[value for i in range(rows)] for j in range(cols)]

class Tree:
    def __init__(self, probability, feature = None, left = None, right = None):
        self.left = left
        self.right = right
        self.probability = probability
        self.feature = feature
        
    def calculate(self, features):
        if self.feature == None:
            return self.probability
        result = self.probability
        if self.feature in features:
            return result * self.left.calculate(features)
        else:
            return result * self.right.calculate(features)
        
        
def readTree(text):
    text = text.strip()
    if text == "":
        return None
    left = text.find("(")+1
    right = text.rfind(")")-1
    text = text[left:right+1]
    text = text.strip()
    
    temp = text.find(" ")
    if temp == -1:
        temp = len(text)
    probability = float(text[:temp])
    
    text = text[temp+1:]
    text = text.strip()
    if text == "":
        return Tree(probability) 
    
    temp = text.find(" ")
    feature = text[:temp]
    
    text = text[temp+1:]
    text = text.strip()
    templist = list(text)
    count = 1
    for i in range(1, len(text)):
        if templist[i] == "(":
            count+=1
        if templist[i] == ")":
            count-=1
        if count == 0:
            break
    lefttext = text[:i+1]
    righttext = text[i+1:]
    lefttree = readTree(lefttext)
    righttree = readTree(righttext)
    return Tree(probability, feature, lefttree, righttree)
    
caseNo = ReadInts()[0]
for case in range(1, caseNo+1):
    L =  ReadInts()[0]
    texttree = ""
    for l in range(L):
        texttree += ifs.readline()+ " "
    texttree.replace("\n", " ")
    texttree = list(texttree)
    for index in range(1, len(texttree)):
        if texttree[index] == " " and texttree[index-1] ==" ":
            texttree[index-1] =="\n"
    texttree = [i for i in texttree if i != "\n"]
    texttree = "".join(texttree)
    tree = readTree(texttree)
    
    A =  ReadInts()[0]
    print  >> ofs, "Case #%d:" % case
    for i in range(A):
        animal = ifs.readline().strip()
        animal = animal.split(" ")
        print >> ofs, "%0.7f" % tree.calculate(animal)
    
    



ifs.close()
ofs.close()



