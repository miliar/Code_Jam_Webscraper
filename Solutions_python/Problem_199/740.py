#!/usr/bin/env python3
def main():
    testcases = int(input())
    for i in range(testcases):
        info = input().strip().split()
        pancakes = list(info[0])
        K = int(info[1])
        result = process_pancakes(pancakes, K)
        if result == "IMPOSSIBLE":
            print_case(i + 1, result)
        else:
            print_case(i + 1, str(result))

def process_pancakes(pancakes, K):
    num_flips = 0
    for idx, val in enumerate(pancakes):
        if val == '-':
            pancakes = invert_pancakes_from(pancakes, idx, K)
            num_flips += 1
            if not pancakes:
                return "IMPOSSIBLE"
    return num_flips

def invert_pancakes_from(pancakes, start, K):
    if start + K - 1 > len(pancakes) - 1:
        return False
    for i in range(start, start + K):
        pancakes[i] = flip(pancakes[i])
    return pancakes

def flip(string):
    if string == '-':
        return '+'
    return '-'

def print_case(name, points):
    string = 'Case #' + str(name) + ': ' + str(points)
    print(string)

if __name__ == '__main__':
    main()
