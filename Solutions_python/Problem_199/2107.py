import sys
import logging
level = logging.INFO
format = '  %(message)s'
handlers = [logging.FileHandler('filename.log'), logging.StreamHandler()]
logging.basicConfig(level = level, format = format, handlers = handlers)

t = int(input())

def solve(pancakes, size):
    flips = 0
    for i in range(len(pancakes) - size + 1):
        if pancakes[i] == 0:
            for j in range(size):
                pancakes[i + j] = 1 - pancakes[i + j]
            flips += 1
    if 0 in pancakes:
        return "IMPOSSIBLE"
    return flips

for i in range(1, t + 1):
    line = sys.stdin.readline().strip("\n")
    pancakes, size = line.split(" ")
    pancakes = [(0 if p == "-" else 1) for p in pancakes]
    solution = solve(pancakes, int(size))
    print("Case #{}: {}".format(i, solution))