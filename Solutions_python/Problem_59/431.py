# Google Code Jam 2010.
# Larry Engholm, 5/22/2010

# Problem description:
# http://code.google.com/codejam/contest/dashboard?c=635101#s=p0
"""
"""
import sys
            
def addDir(root, dir):
    parent = root
    count = 0
    for comp in dir.split('/'): # component
        if not comp in parent:
            parent[comp] = {}
            count += 1
        parent = parent[comp]
    return count

def calculate(root, newdirs):
    count = 0
    for dir in newdirs:
        count += addDir(root, dir)
    return count

def main():
    file = open('c:/Documents and Settings/Larry/My Documents/Downloads/A-large.in')
    numTests = int(file.readline())
    for i in range(numTests):
        root = {}
        newdirs = []
        (numExisting, numNew) = map(int, file.readline().split())
        for j in range(numExisting):
            addDir(root, file.readline().strip()[1:])
        for k in range(numNew):
            newdirs.append(file.readline().strip()[1:])
        print 'Case #{0}: {1}'.format(i+1, calculate(root, newdirs))
main()
