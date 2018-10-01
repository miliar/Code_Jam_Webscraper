count = int(raw_input())
for i in range(count):
    num = raw_input()
    res = num
    for digP in range(len(num) - 1):
        digit = num[digP]
        digitN = num[digP + 1]
        if int(digitN) < int(digit):
            digT = digP
            while digT > 0:
                if num[digT] == num[digT-1]:
                    digT = digT-1
                else:
                    break
            res = num[0:digT] + str(int(num[digT]) - 1) + '9'*(len(num)- digT - 1)
            break
    if res[0]!='0':
        print "Case #" + str(i + 1) + ": " +res
    else:
        print "Case #" + str(i + 1) + ": " +res[1:len(res)]
