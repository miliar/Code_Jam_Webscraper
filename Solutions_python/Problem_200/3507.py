f = open('in.txt', 'r')
out = open('out.out', 'w')

count = 0
for line in f:
    if count == 0:
		count += 1
		continue
    length = len(line.strip())
    string = list(line.strip())
    not_done = True
    while not_done:
        if length == 1:
            break
        for i in range(1, length):
            if string[length - i] < string[length - (i + 1)]:
                string[length - (i + 1)] = str(int(string[length - (i + 1)]) - 1)
                for j in range(length - i, length):
                    string[j] = '9'
                break
            if i == length - 1:
                not_done = False
    result = ''.join(string)
    n = str(long(result))
    out.write('Case #' + str(count) + ': ' + n + '\n')
    count += 1

f.close()
out.close()
