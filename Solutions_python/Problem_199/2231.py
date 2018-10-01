from collections import deque
from sys import stdin
lines = deque(line.strip() for line in stdin.readlines())

def nextline():
    return lines.popleft()

def types(cast):
    return tuple(int(x) for x in nextline().split())

def ints():
    return types(int)

def strs():
    return nextline().split()

def ishappy(ch):
    return ch == '+'

def main():
    # lines will now contain all of the input's lines in a list
    T = int(nextline())
    for testCase in range(1, T + 1):
        pancakes, K = strs()
        pancakes = list(map(ishappy, pancakes))
        K = int(K)
        count = 0
        for i in range(len(pancakes)-K+1):
            if not pancakes[i]:
                for j in range(K):
                    pancakes[i+j] = not pancakes[i+j]
                count += 1
        print("Case #{}: {}".format(testCase, "IMPOSSIBLE" if False in pancakes[-K+1:] else count))
        

if __name__ == '__main__':
    main()
