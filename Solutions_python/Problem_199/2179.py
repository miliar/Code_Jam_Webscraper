import sys
import glob


def flip(p):
    return "+" if p == "-" else "-"


def countFlips(s, K):
    stack = list(s)
    stackSize, count = len(s), 0

    for i in range(stackSize - 1, -1, -1):
        if stack[i] == "+": continue
        for j in range(0, int(K)):
            if i - j < 0: return "IMPOSSIBLE"
            stack[i-j] = flip(stack[i-j])
        count += 1

    return str(count)

if len(sys.argv) != 2:
    print("Please enter an input file.")
    exit()

inputFiles = []
if str(sys.argv[1]) == "-l": inputFiles = glob.glob('*-large*.in')
elif str(sys.argv[1]) == "-s": inputFiles = glob.glob('*-small*.in')
elif str(sys.argv[1]) == "-t": inputFiles = glob.glob('*.in')
else:
    print("Unknown command.")
    exit()

for fn in inputFiles:
    with open(fn) as f:
        T = int(f.readline())
        lines = [line.strip() for line in f.readlines()]
        stack = [line.split(" ")[0] for line in lines]
        K = [line.split(" ")[1] for line in lines]

        for x in range(0, T):
            print("Case #" + str(x+1) + ": " + countFlips(stack[x], K[x]))