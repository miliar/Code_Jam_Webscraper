
import math

def outputData(caseNum, count, output):
    output.write("Case #" + str(caseNum + 1) + ": " + str(count) + "\n")

def isPalindrome(num):
    num = str(num)
    return num == num[::-1]

#===============================================

mi = 1
ma = int(math.sqrt(100000000000000))
palindromes = []
for num in range(mi, (ma + 1)):
    if isPalindrome(num) and isPalindrome(num*num):
        palindromes.append(num*num)
#===============================================
            
input_file = open("C-large-1.in")
output = open('output.txt', 'w')

input_data = input_file.read()
data = input_data.split()
for i in range(len(data)):
    data[i] = int(data[i])
cases = data.pop(0)
for case in range(cases):
    minimum = data.pop(0)
    maximum = data.pop(0)
    count = 0
    for palindrome in palindromes:
        if palindrome >= minimum and palindrome <= maximum:
            count += 1
    outputData(case, count, output)
output.close()
        
