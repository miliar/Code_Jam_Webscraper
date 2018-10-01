def flip(pancakes, K, start):
    for i in range(start, start+K):
        if pancakes[i] == "+":
            pancakes[i] = "-"
        else:
            pancakes[i] = "+"
    return pancakes

# let minflips(pancakes, K, start) be a function that returns the
# number of flips needed (or impossible) where the pancakes have flip
# state described by pancakes, the flipper has size K, and only the
# startth+ pancake can be flipped
# if minflips returns 10000, then it's impossible
def minflips(pancakes, K, start):
    if "-" not in pancakes:
        return 0
    if start+K > S: return 10000
    best = 10000
    flippednext = flip(pancakes[:], K, start)
    skippednext = pancakes[:]
    if "-" not in pancakes[start:start+K]:
        return min(best, minflips(skippednext, K, start+1))
    best = min(best, minflips(flippednext, K, start+1) + 1)
    best = min(best, minflips(skippednext, K, start+1))
    return best

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    line, K = input().split(" ")
    K = int(K)
    line = list(line)
    S = len(line)
    out = minflips(line, K, 0) 
    if out == 10000:
        out = "IMPOSSIBLE"
    print("Case #{}: {}".format(i, out))

  # check out .format's specification for more formatting options 
