"""
    Oh yeah
"""
from sets import Set

def pancake_flip_count(pancakes, K):
    n = len(pancakes)
    flips = 0
    for i in range(n - K + 1):
        if pancakes[i] == '-':
            flips += 1
            for j in range(i, i + K):
                if pancakes[j] == '-':
                    pancakes[j] = '+'
                else:
                    pancakes[j] = '-'
    if any(map(lambda x : x == '-', pancakes)):
        return 'IMPOSSIBLE'
    return flips

with open('A-large.in') as file:
    with open('output.raw' ,'w') as ofile:
        n = int(file.readline())
        i = 1
        for line in file:
            split_line = line.split()
            K = int(split_line[1])
            pancakes = list(split_line[0])
            ofile.write('Case #{}: {}\n'.format(i, pancake_flip_count(pancakes, K)))
            i += 1
