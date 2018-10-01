#author: calmcoder@gmail.com

fileName = 'A-large.in'

file = open(fileName, 'r')
T = int(file.readline())

for i in range(1,T + 1):
    light = 'OFF'
    nextLine = file.readline().rstrip().split(' ')
    n = int(nextLine[0])
    k = int(nextLine[1])
    if(k == 0):
        light = 'OFF'
    elif((n == 1) and ((k + 1) % 2) == 0):
        light = 'ON'
    elif((((k+1) % 2**n) == 0) and ((k + 1) >= 2 ** n)):
        light = 'ON'
    print 'Case #' + str(i) + ': ' + light
    