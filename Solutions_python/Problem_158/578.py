# Google Code Jam
prefix = './C/'
inputFile = open(prefix + 'D-small-attempt0.in', 'r')
outFile = open(prefix + 'out.out', 'w')

# Number of test cases
T = int(inputFile.readline())

# Read in each row
for counter in range(T):
    line = list(map(int, inputFile.readline().split()))

    # Type of X-omino
    X = line[0]

    # Dimensions of grid that must be filled
    R = min(line[1], line[2])
    C = max(line[1], line[2])

    # X == 1 always has GABRIEL winning (only 1x1 block)
    winner = "GABRIEL"

    # Only 2x1 block
    if X == 2 and R * C % 2 != 0:
        winner = "RICHARD"

    # Only 3x1 block or corner block
    elif X == 3:
        if R == 1:
            winner = "RICHARD"
        elif R * C % X != 0:
            winner = "RICHARD"

    # 5 different types
    elif X == 4:
        if R == 1:
            winner = "RICHARD"
        elif R == 2:
            winner = "RICHARD"
        elif R * C % X != 0:
            winner = "RICHARD"

    outFile.write("Case #" + str(counter+1) + ": " + winner + "\n")

outFile.close()
