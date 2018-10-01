inputF = open('A-large.in', 'r')
output = open('A-large.out', 'w')


def countFlips(pancakes, width):
    count = 0
    for i in range(len(pancakes)-width+1):
        if pancakes[i] == '-':
            count += 1
            for j in range(width):
                if pancakes[i+j] == '+':
                    pancakes = pancakes[:i+j] + '-' + pancakes[i+j+1:]
                else:
                    pancakes = pancakes[:i+j] + '+' + pancakes[i+j+1:]

    for i in range(len(pancakes)-width+1, len(pancakes)):
        if pancakes[i] == '-':
            return 'IMPOSSIBLE'

    return str(count)



numCases = int(inputF.readline())

for i in range(numCases):
    line = inputF.readline().split()
    pancakes = line[0]
    width = int(line[1])
    
    numFlips = countFlips(pancakes, width)

    output.write('Case #' + str(i+1) + ': ')
    output.write(numFlips + '\n')

inputF.close()
output.close()
