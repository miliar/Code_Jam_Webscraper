import sys

inputFile = sys.argv[1]

with open(inputFile, "r") as f:
    T = int(f.readline())
    for test in range(1, T + 1):
        row1 = int(f.readline()) - 1
        rows = []
        for i in range(4):
            rows.append(map(int, f.readline().strip().split()))
        set1 = set(rows[row1])
        
        row2 = int(f.readline()) - 1
        rows = []
        for i in range(4):
            rows.append(map(int, f.readline().strip().split()))
        set2 = set(rows[row2])
        
        answers = set1 & set2
        
        if answers:
            if len(answers) == 1:
                output = list(answers)[0]
            else:
                output = "Bad magician!"
        else:
            output = "Volunteer cheated!"
        print "Case #{0}: {1}".format(test, output)