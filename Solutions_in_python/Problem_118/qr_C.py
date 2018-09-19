import math

palindromes = {}
palindromes[1] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def generatePalindromesInInterval(start, end):
    startDigits = len(str(start))
    endDigits = len(str(end))
    palinList = []
    for digits in range(startDigits, endDigits+1):
        if digits not in palindromes: generatePalindromes(digits) 
        palinList.extend(palindromes[digits])
    palinListInt = filter(lambda x: x>= start and x<= end, map(int, palinList))
    return palinListInt
    
def generatePalindromes(digits):
    palinList = []    
    if digits%2==1: # if odd
        if digits-1 not in palindromes: generatePalindromes(digits-1)
        for singleDigit in palindromes[1]:
            for pal in palindromes[digits-1]:
                palinList = pal[:(digits-1)/2] + singleDigit + pal[(digits-1)/2:]
    else: # if even
        for i in range(10**((digits/2)-1), 10**(digits/2)):
            newPalin = str(i)+str(i)[::-1]
            if newPalin[0] != '0': palinList.append(newPalin)
    palindromes[digits] = palinList
    
def isPalindrome(num):
    return (str(num) == str(num)[::-1])

fInput = open("C-small-attempt0.in", 'r')
fOutput = open("C-small-attempt0.out", 'w')

num_cases = int(fInput.next())

for case in range(1,num_cases+1):
    if case%((num_cases/10) if num_cases>=10 else 1)==0: print '.',
    start, end = map(int, fInput.next().split())
    rootStart = int(math.ceil(math.sqrt(start)))
    rootEnd = int(math.floor(math.sqrt(end)))
    rootPalinList = generatePalindromesInInterval(rootStart, rootEnd)
    count = 0
    for rootPalin in rootPalinList:
        if isPalindrome(rootPalin*rootPalin):
            count += 1
    out_str = str(count)
    fOutput.write("Case #{0}: ".format(case) + out_str + "\n")
    
fInput.close()
fOutput.close()
print "\t[DONE]"