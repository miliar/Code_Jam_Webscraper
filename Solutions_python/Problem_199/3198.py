class Tree:
    def __init__(self, k, pancakes):
        self.value = list(pancakes)
        self.n = len(pancakes)
        self.k = k
        self.selections = self.n - k + 1
        self.children = []
        self.depth = 0
        self.allSidesUp = False

    def make_children(self):
        for i in range(self.selections):
            new_pancakes = self.value[:]
            for j in range(self.k):
                if new_pancakes[i+j] == "+":
                    new_pancakes[i+j] = "-"
                else:
                    new_pancakes[i+j] = "+"
            child = Tree(self.k, "".join(new_pancakes))
            child.depth = self.depth + 1
            self.children.append(child)
            if "".join(new_pancakes) == "+"*self.n:
                self.allSidesUp = True

    def getValue(self):
        return "".join(self.value)

    def ifAllSideUp(self):
        return self.allSidesUp

    def print_children(self):
        for child in self.children:
            print("Pancakes: " + "".join(child.value))

def solution(root):
    toExplore = {root}
    visited = {root.getValue()}
    while len(toExplore) != 0:
        newExplore = set()
        for node in toExplore:
            node.make_children()
            if node.ifAllSideUp():
                return node.depth + 1
            for child in node.children:
                if child.getValue() not in visited:
                    visited.add(child.getValue())
                    newExplore.add(child)
        toExplore = newExplore
    return -1

file = open('input.txt')
tests = int(file.readline())
cases = []
for t in range(tests):
    cases.append(file.readline().strip().split(' '))
test = 0
for pancakes, k in cases:
    test += 1
    answer = 0
    if not len(pancakes)*"+" == pancakes:
        root = Tree(int(k), pancakes)
        answer = solution(root)
    if answer != -1:
        print("Case #{}: {}".format(test, answer))
    else:
        print("Case #{}: IMPOSSIBLE".format(test))







