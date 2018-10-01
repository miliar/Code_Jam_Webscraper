#!/usr/bin/env python

class node():
    def __init__(self,name):
        self.name = name
        self.children = []
    def __str__(self):
        return self.name

    def create(self, directory):
#        print self.name, ' has ',
#       for item in self.children:
#            print item
#        print '-------------'
        if len(directory) == 0:
            return 0
        for i in range(len(self.children)):
            if self.children[i].name == directory[0]:
#                print 'found', directory[0],' in ',self.name
                return self.children[i].create(directory[1:])
        self.children.append(node(directory[0]))
#        print 'add',directory[0],' in ',self.name
        return 1 + self.children[-1].create(directory[1:])

        

def main():
    fin = open('large.in','r')
    fout = open('large.out','w')
    t = int(fin.readline())
    for test in range(t):
        n,m = fin.readline().split(' ')
        n = int(n)
        m = int(m)
        exists = []
        creates = []

        for i in range(n):
            exists.append(fin.readline()[:-1].split('/')[1:])
        for i in range(m):
            creates.append(fin.readline()[:-1].split('/')[1:])
        
#        print t,' ',n,' ',m
#        print exists
#        print creates
        #input done
        
        root = node('')
        for directory in exists:
            root.create(directory)
        count = 0
        for directory in creates:
            count += root.create(directory)
        
        fout.write('Case #%d: %d\n' % (test+1,count))

if __name__ == '__main__':
    main()
