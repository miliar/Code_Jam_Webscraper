inputFile = open('B-small-attempt0.in', 'rb')

outputFile = open('B-small-attempt0.out', 'w')

T = int(inputFile.readline().rstrip("\n"))

for t in range(0, T):

    row = inputFile.readline().rstrip("\n").split(" ")

    A = int(row[0])

    B = int(row[1])

    K = int(row[2])

    if B < A:
        A, B = B, A

    count = 0

    for i in range(0, A):
        for j in range(0, B):
            if (i&j) < K:
                count += 1

    outputFile.write("Case #%d: %d\n" % (t+1, (count)))
