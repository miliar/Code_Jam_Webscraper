#!/usr/bin/env python3

def main():
    #"The first line of the input gives the number of test cases, T."
    t = int(input())
    for i in range(t):
        #"Each consists of one line with a string S and an integer K. S represents the row of pancakes: each of its characters is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up)."
        s, k = input().split()
        pancakes = [int(c + '1') for c in s]
        k = int(k)
        
        ans = solve(pancakes, k)
        #"For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is either IMPOSSIBLE if there is no way to get all the pancakes happy side up, or an integer representing the the minimum number of times you will need to use the oversized pancake flipper to do it."
        print("Case #%d: %s" % (i+1, ans))


def solve(pancakes, k):
    # 2 <= k <= len(pancakes)
    " Given the current state of the pancakes, calculate the minimum number of uses of the oversized pancake flipper needed to leave all pancakes happy side up, or state that there is no way to do it."
    count = 0
    for i in range(len(pancakes) - k + 1):
        if pancakes[i] < 0:
            flip(pancakes, i, k)
            count += 1
    if sum(pancakes) != len(pancakes):
        return "IMPOSSIBLE"
    return count


def flip(pancakes, i, k):
    for j in range(i, i+k):
        pancakes[j] *= -1


main()
