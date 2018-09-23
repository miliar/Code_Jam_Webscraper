import os

case_num = 1

def flipper(pancakes, size):
    kitchen = []
    for i in range(0, len(pancakes)):
        if pancakes[i] == '+':
            kitchen.append('+')
        if pancakes[i] == '-':
            kitchen.append('-')
    flips = 0
    while kitchen.count('-') > 0:    
        for i in range(0, len(kitchen) - size + 1):
            if kitchen[i] == '-':
                for j in range(i, i + size):
                    if kitchen[j] == '-':
                        kitchen[j] = '+'
                        continue
                    elif kitchen[j] == '+':
                        kitchen[j] = '-'
                flips += 1
        for t in range(0, len(kitchen))[(-size+1):]:
            if kitchen[t] == '-':
                return 'IMPOSSIBLE'
    return flips
        

##def flipper2(pancakes, size):
##    kitchen = []
##    for i in range(0, len(pancakes)):
##        if pancakes[i] == '+':
##            kitchen.append(0)
##        if pancakes[i] == '-':
##            kitchen.append(1)
##    flips = 0
##    while kitchen.count('-') > 0:    
##        for i in range(0, len(kitchen))[-3:]:
##            if kitchen[i] % 2 == 1:
##                for j in range(i, i + size):
##                    kitchen[j] += 1
##                flips += 1
##        if kitchen[-1] % 2 == 1:
##            return 'IMPOSSIBLE'
##    return flips             


with open('A-large.in', 'rb') as text_file:
    t = text_file.readline().strip('\r\n')
    for line in text_file:
        line = line.strip('\r\n').split()
        N = line[0]
        K = int(line[1])
        print 'Case #%s: %s' % (case_num, flipper(N, K))
        case_num += 1



