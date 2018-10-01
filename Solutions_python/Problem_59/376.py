# usage : file.py problem_instance.in

def clean(s):
    if s[len(s)-1:]=='\n':
        return s[0:len(s)-1]

class Tree :

    def __init__(self, directory, subdirectories, n):
        self.directory = directory
        self.subdirectories = subdirectories
        self.n = n
        self.leaf = True
        self.newBranch = 0

    def buildTree(self, path, root):
        if path == [] :
            return
        for tree in self.subdirectories :
            if path[0] == tree.directory :
                tree.buildTree(path[1:], root)
                break
        else :
            t = Tree(path[0], [], 0)
            t.buildTree(path[1:], root)
            self.subdirectories.append(t)
            root.n += 1

class File:

    def __init__(self,argv):
        self.argv = argv
        self.number = 0
        self.case = 0
        self.out = ''
        self.given = 0
        self.mkdir = 0
        self.tree = Tree('/', [], 0)
        self.input()

    def input(self):
        f = open(self.argv,'r')
        self.lines = f.readlines()
        f.close()
        self.number = int(self.lines[0])
        self.lines = self.lines[1:]

    def output(self):
        sys.stdout.write(self.out)
        file = self.argv.split('.in')[0]+'.out'
        f = open(file,'w')
        f.writelines(self.out)
        f.close()

    def do(self):
        self.tree = Tree('/', [], 0)
        self.newcase = self.lines[0].split(' ')
        self.given = int(self.newcase[0])
        self.mkdir = int(self.newcase[1])
        self.lines = self.lines[1:]
        self.addGiven(self.given)
        self.tree.n = 0
        self.addMkdirs(self.mkdir)

    def addGiven(self, n):
        if (n==0) :
            return
        self.buildTree(self.lines[0])
        self.lines = self.lines[1:]
        self.addGiven(n-1)

    def addMkdirs(self, n):
        if (n==0) :
            return
        self.buildTree(self.lines[0])
        self.lines = self.lines[1:]
        self.addMkdirs(n-1)

    def buildTree(self, path):
        dirs = clean(path).split('/')[1:]
        self.tree.buildTree(dirs, self.tree)
    
    def Run(self):
        for i in range(0, self.number):
            self.do()
            self.case += 1
            self.out += 'Case #'+str(self.case)+': '+str(self.tree.n)+'\n'
        self.output()

if __name__ == "__main__":
    import sys
    file = File(sys.argv[1])
    file.Run()
    sys.exit(0)
