import sys
f = open(sys.argv[1], 'r')
T = int(f.readline())
for t in range(T):
    answer = int(f.readline()) - 1
    matrix = [f.readline().split(), f.readline().split(), f.readline().split(), f.readline().split()]
    for i in range(4):
        for j in range(4):
            matrix[i][j] = int(matrix[i][j])
    possible1 = set(matrix[answer])
            
    answer = int(f.readline()) - 1
    matrix = [f.readline().split(), f.readline().split(), f.readline().split(), f.readline().split()]
    for i in range(4):
        for j in range(4):
            matrix[i][j] = int(matrix[i][j])
    possible2 = set(matrix[answer])

    possible = possible1.intersection(possible2)

    print "Case #%d: " % (t + 1),
    if not possible:
        print "Volunteer cheated!"
    elif len(possible) > 1:
        print "Bad magician!"
    else:
        print possible.pop()
