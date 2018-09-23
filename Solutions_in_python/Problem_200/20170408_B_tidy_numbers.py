with open('B-large.out', 'w') as output:
    with open('B-large.in', 'r') as input:
        n = int(input.readline(-1).strip())
        for i in range(n):
            numbers = input.readline(-1).strip()
            a = numbers[0]
            k = 1
            flag = 0
            while(k != len(numbers)):
                if(numbers[k] >= a):
                    a = numbers[k]
                    k += 1
                    continue
                else:
                    flag = -1
                    break
            if flag == 0:
                output.write("Case #%d: %s\n" % (i+1, numbers))
                continue
            else:
                numbers = "%s%s" % (numbers[:k], '9'*(len(numbers)-k))
                k -= 1
                while(k >= 0):
                    if(numbers[k] > '1'):
                        if k > 0 and numbers[k-1] == numbers[k]:
                            numbers = '%s9%s' % (numbers[:k], numbers[k + 1:])
                            k -= 1
                        else:
                            numbers = '%s%s%s' % (numbers[:k], str(int(numbers[k])-1), numbers[k+1:])
                            break
                    elif k == 0:
                        numbers = numbers[1:]
                        break
                    else:
                        numbers = '%s9%s' % (numbers[:k], numbers[k+1:])
                        k -= 1
                output.write("Case #%d: %s\n" % (i+1, numbers))



