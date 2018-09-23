# Problem 01 - Oversize Pancake Flipper


read = open('A-large.in', 'r')
write = open('A-large.out', 'w')

T = 0
K = 0
S = ''
count = 0
case = 1
line_count = -1
impossible = False

for line in read:
    line_count += 1
    if int(line_count) is 0:
        T = line
    elif int(line_count) <= int(T):
        split_data = line.split(' ')
        S = split_data[0]
        K = split_data[1]
        listS = list(S)
        for i in range(0, len(listS)):
            if str(listS[i]) is '-':
                if (i + int(K)) <= len(listS):
                    for j in range(0, int(K)):
                        pos = i + j
                        if str(listS[pos]) is '-':
                            listS[pos] = '+'
                        else:
                            listS[pos] = '-'
                    count += 1
                    i = 0
                else:
                    impossible = True

        if impossible:
            write.write('Case #' + str(case) + ': IMPOSSIBLE \n')
            case += 1
            count = 0
            impossible = False
        else:
         write.write('Case #' + str(case) + ': ' + str(count) + '\n')
         case += 1
         count = 0

read.close()
write.close()
