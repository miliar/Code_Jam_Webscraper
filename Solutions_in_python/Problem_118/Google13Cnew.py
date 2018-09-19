import urllib2
import bisect
import math

def search(list, x):
    n = len(list)
    if n == 1:
        return int(x > list[0])
    else:
        mid = n/2
        if x <= list[mid]:
            return search(list[:mid], x)
        else:
            return search(list[mid:], x) + mid

def isPalin(n):
    string = str(n)
    m = len(string)
    for i in range(m/2):
        if string[i] != string[m-1-i]:
            return False
            break
    else:
        return True

rootStrings = ["", "0", "1", "2", "3"]
i = 0
while len(rootStrings[-1]) < 52:
    rootStrings.append('0' + rootStrings[i] + '0')
    for r in ['1', '2']:
        st = r + rootStrings[i] + r
        if isPalin(int(st) ** 2):
            rootStrings.append(st)
    i += 1

roots = []
for x in rootStrings[1:]:
    if x[0] != '0':
        roots.append(int(x))
roots.sort()

solutions = [x**2 for x in roots]

f = open("dataIn.txt", 'r')
g = open("dataOut.txt", 'w')

t = int(f.readline())

for i in range(t):
    line = f.readline()
    a, b = (int(x) for x in line.split(' '))
    l = search(solutions, a)
    r = search(solutions, b)
    result = r-l
    if b == solutions[r]:
        result += 1
    g.write("Case #" + str(i+1) + ": " + str(result) + '\n')
f.close()
g.close()

print "Done."
