t = int(input().strip()) # num testcases
for c in range(t):
    testcase = input().strip().split()
    pancakes = list(testcase[0])
    length = int(testcase.pop())
    
    count = 0
    for i in range(len(pancakes) - length + 1):
        if pancakes[i] == '-':
            count += 1 # flip
            for j in range(length):
                if pancakes[i+j] == '-':
                    pancakes[i+j] = '+'
                else:
                    pancakes[i+j] = '-'
    isPossible = 0
    for i in pancakes:
        if i == '-':
            isPossible = 1
            break
    if isPossible:
        print('Case #' + str(c + 1) + ': IMPOSSIBLE')
    else:
        print('Case #' + str(c + 1) + ': ' + str(count))