import math

def main():
    f = open("A-large.in")
    tests = int(f.readline())
    for i in range(tests):
        line = f.readline()
        x = line.split(" ")
        pancakes = x[0]
        k = int(x[1])
        numflips = computeFlips(pancakes, k)
        result = str(numflips) if numflips!=-1 else "IMPOSSIBLE"
        print("Case #{0}: {1}".format(i+1, result))

def computeFlips(pancakes, k):
    if isHappy(pancakes):
        return 0

    indices = []
    for i in range(len(pancakes)-k+1):
        if pancakes[i] == "-":
            pancakes = flip(pancakes, i, k)
            indices.append(i)
            if(isHappy(pancakes)):
                break

    if isHappy(pancakes):
        return len(indices)
    else:
        return -1


def flip(pancakes, index, k):
    newpancakes = ""
    newpancakes += pancakes[:index]
    for i in range(k):
        newpancakes += "+" if pancakes[index] == "-" else "-"
        index += 1
    newpancakes += pancakes[index:]
    return newpancakes

def isHappy(pancakes):
    for s in pancakes:
        if s != "+":
            return False
    return True


if __name__ == "__main__":
    main()
