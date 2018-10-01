class tree:
    def __init__(self, weight):
        self.weight = float(weight)
        self.feature = None
        self.yes = None
        self.no = None
    def __repr__(self):
        return "<Tree " + str(self.weight) + (" " + self.feature if self.feature else "") + (" " + repr(self.yes) if self.yes else "") \
            + (" " + repr(self.no) if self.no else "") + ">"

def readTree(text, index):
    while text[index] != "(":
        index += 1
    while not text[index].isdigit():
        index += 1
    weight = ""
    while text[index] != " " and text[index] != ")":
        weight += text[index]
        index += 1
    while text[index] == " ":
        index += 1
    node = tree(weight)
    if text[index] == ")":
        return node, index
    feature = ""
    while text[index].isalpha():
        feature += text[index]
        index += 1
    node.feature = feature
    node.yes, index = readTree(text, index)
    node.no, index = readTree(text, index)
    return node, index

def howCute(node, p, a):
    p *= node.weight
    if node.feature == None:
        return p
    if node.feature in a[1]:
        return howCute(node.yes, p, a)
    else:
        return howCute(node.no, p, a)

infile = open("A-large.in")
outfile = open("A-large.out", "w")
N = int(infile.readline())
for testcaseN in range(N):
    L = int(infile.readline())
    treeText = ""
    for i in range(L):
        treeText += infile.readline().strip()
    root = readTree(treeText, 0)[0]
    A = int(infile.readline())
    animals = []
    for i in range(A):
        text = infile.readline().split()
        name = text[0]
        attributes = []
        for j in range(int(text[1])):
            attributes.append(text[j + 2])
        animals.append((name, attributes))
    results = {}
    for a in animals:
        p = 1.0
        node = root
        results[a[0]] = howCute(node, p, a)
    outfile.write("Case #" + str(testcaseN + 1) + ":\n")
    for a in animals:
        outfile.write(("%.7f" % results[a[0]]) + "\n")
        