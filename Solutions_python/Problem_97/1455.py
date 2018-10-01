def find_combinations(lower, num, upper):
    numbers = []
    number = []
    number.extend(num)
    for i in range(0, len(number)-1):
        pre = ''
        number = []
        number.extend(num)
        for a in range(len(number) - 1, len(number) - 2 - i, -1):
            pre += number.pop()
        no = int(pre[::-1] + ''.join(map(str, number)))
        if no >= lower and no <= upper and no not in numbers and no > int(''.join(map(str, num))):
            print '(',int(''.join(map(str, num))),',', no ,')'
            numbers.append(no)
    return len(numbers)

fp = open('inputs.txt', 'r')
inputs = fp.readlines()
fp.close()
fp = open('output.txt', 'w')
cases = int(inputs[0].strip('\n'))
for i in range(1, cases + 1):
    line = inputs[i].strip('\n').split()
    a = int(line[0])
    b = int(line[1])
    res = 0

    print a, b
    for l in range(a, b + 1):
        number = list(str(l))
        # now we got the number lets permute it
        res += find_combinations(a, number, b)
    fp.write('Case #%d: ' % i + str(res) + '\n')
