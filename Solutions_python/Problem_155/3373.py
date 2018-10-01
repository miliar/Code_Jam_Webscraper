name = 'A-large'
file = open(name + '.in', 'r')
c = int(file.readline())
result = list()
for tt in range(c):
    data = file.readline()
    n = data.split(' ')

    count = 0

    sum = int(n[1][0])

    for i in range(1, int(n[0])+1):
        value = int(n[1][i])
        if value > 0 and i > sum:
            count += i - sum
            sum = i
        sum += value
    result.append(count)
    
file.close()
file = open(name + '.out', 'w')
for i in range(len(result)):
    file.write('Case #' + str(i + 1) + ': ' + str(result[i]) + '\r\n')