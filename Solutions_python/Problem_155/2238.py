__author__ = 'Glen'
numCases = int(input().strip())
for caseNum in range(numCases):
    sMax, line = input().strip().split()
    total = 0
    needed = 0
    for idx, char in enumerate(line):
        if total < idx:
            needed += idx - total
            total = idx
        total += int(char)
    print('Case #{}: {}'.format(caseNum+1, needed))
