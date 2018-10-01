def istidy(number):
    stringnumber = str(number)
    digits = len(stringnumber)
    if(digits == 1):
        return True
    for i in range(1, digits):
        if int(stringnumber[i]) < int(stringnumber[i - 1]):
            return False
    return True

def getresult(number):
    result = number
    while not istidy(result):
        result -= 1
    return result

def getresultadv(number):
    digits = list(map(int, str(number)))
    digits_num = len(str(number))
    problemindex = -1
    for i in range(1, digits_num):
        if digits[i - 1] > digits[i]:
            problemindex = i - 1
            break
    if problemindex == -1:
        return str(number)
    current_index = problemindex + 1
    digits.insert(0, 0)
    while not digits[current_index - 1] <= digits[current_index] - 1:
        current_index -= 1
    digits[current_index] -= 1
    for i in range(current_index + 1, len(digits)):
        digits[i] = 9
    stringdigits = list(map(str, digits))
    returnvalue = ''
    wasnonzero = False
    for item in stringdigits:
        if item == '0' and not wasnonzero:
            pass
        else:
            returnvalue += item
            wasnonzero = True
    return returnvalue

t = int(input())

for i in range(t):
    number = int(input())
    print("Case #"+str(i + 1)+": " + str(getresultadv(number)))
