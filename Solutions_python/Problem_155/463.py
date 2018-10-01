import sys
# sys.stdin = open('in.txt','r')
# sys.stdout = open('out.txt', 'w')

def doCase(line,currentCase):
    friends = 0
    parts = line.split()
    Smax = int(parts[0])
    people = parts[1]
    standing = 0

    for Si in range(Smax+1):
        if Si > standing:
            friends += Si - standing
            standing = Si
        standing += int(people[Si])

    print "Case #{}: {}".format(currentCase,friends)



caseNum = int(sys.stdin.readline())
for i in range(caseNum):
    doCase(sys.stdin.readline(),i+1)

