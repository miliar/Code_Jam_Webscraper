import os

input_file = open("input_large.in", "r")
output_file = open("output_large.out", "w")

cases = int(input_file.readline())

for i in range(cases):

    numArr = list(input_file.readline())
    if numArr[-1] == "\n":
        numArr = numArr[:-1]

    digits = len(numArr)
    for j in range(digits)[:-1]:
        index = digits - (j + 1)
        last_digit = numArr[index]
        cur_digit = numArr[index-1]
        if int(cur_digit) > int(last_digit):
            numArr[index-1] = int(numArr[index-1]) - 1
            for k in range(index, digits):
                numArr[k] = 9

    numArr = map(str, numArr)
    numArr = ''.join(numArr)
    numArr = long(numArr)

    output_file.write("Case #" + str(i + 1) + ": " + str(numArr) + "\n")






