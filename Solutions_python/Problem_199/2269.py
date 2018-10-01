import sys

sys.setrecursionlimit(1500)

def flip(row, size):
    inverse = {"+": "-", "-": "+"}
    for i in range(size):
        row[i] = inverse[row[i]]

def minFlips(row, size):
    if size > len(row):
        if row == ["+"] * len(row):
            return 0
        return float("-inf")
    if row[0] == "+":
        return minFlips(row[1:], size)
    flip(row, size)
    return minFlips(row[1:], size) + 1

with open("input.in") as finput, open("output.out", "w") as foutput:
    numCases = int(finput.readline().strip())
    for i in range(1, numCases + 1):
        row, size = finput.readline().strip().split()
        row = list(row)
        size = int(size)
        answer = minFlips(row, int(size))
        if answer == float("-inf"):
            answer = "IMPOSSIBLE"
        foutput.write("Case #" + str(i) + ": " + str(answer) + "\n")
