#!/usr/bin/env python

def flipsToMakeHappy(pancakes, k):
    num = len(pancakes)
    pancakes = list(pancakes)
    flips = 0
    if num < k:
        return False
    for i in range(num-k+1):
        if pancakes[i] == "-":
            flips += 1
            for j in xrange(i, i+k):
                flip(pancakes, j)

    for p in pancakes:
        if p == "-":
            return "IMPOSSIBLE"

    return flips


def flip(pancakes, index):
    if pancakes[index] == "-":
        pancakes[index] = "+"
    else:
        pancakes[index] = "-"

# def tests():
#     print(flipsToMakeHappy("-+", 2) == "IMPOSSIBLE")
#     print(flipsToMakeHappy("--", 2) == 1)
#     print(flipsToMakeHappy("---+-++-", 3) == 3)
#     print(flipsToMakeHappy("+++++", 4) == 0)
#     print(flipsToMakeHappy("-+-+-", 4) == "IMPOSSIBLE")

# tests()

def main():
    num_problems = int(raw_input())
    for i in xrange(1, num_problems+1):
        line = raw_input().split(" ")
        pancakes, k = line[0], int(line[1])
        print "Case #{}: {}".format(i, flipsToMakeHappy(pancakes, k))

if __name__ == "__main__":
    main()