__author__ = 'Xapheus'

f = open("input.in", 'r')
o = open("output.txt", 'w')
num_cases = int(f.readline())

count = 0
standing = 0
currentShy = 0

for i in range(num_cases):
    a = f.readline().split(' ')
    for j in a[1]:
        if j != '\n':
            if standing < currentShy:
                toAdd = currentShy - standing
                count += toAdd
                standing += toAdd
            standing += int(j)
        currentShy+=1
    o.write("Case #" + str(i+1) + ": " + str(count) + "\n")
    count = 0
    standing = 0
    currentShy = 0

