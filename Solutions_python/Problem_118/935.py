def reversed(num):
    stringy = str(num)
    rev = ''
    for i in range(-1,-len(stringy)-1,-1):
        rev = rev + stringy[i]

    return rev

def IsPalindrome(num):
    stringy = str(num)
    for i in range(0,len(stringy)//2):
        if (stringy[i] != stringy[-i-1]):
            return False
    return True

def GetFairSqures(limit):
    FS = []

    for i in range(1,4):
        if (IsPalindrome(i ** 2)):
            FS.append(i ** 2)
        
    for i in range (1,limit):
        for j in range(0,10):
            palindromestring = str(i) + str(j) + str(reversed(i))
            num = int(palindromestring)
            if (IsPalindrome(num **2)):
                FS.append(num ** 2)
                
        palindromestring2 = str(i) + str(reversed(i))
        num2 = int(palindromestring2)
        if (IsPalindrome(num2 **2)):
            FS.append(num2 ** 2)

    FS.sort()
    return FS

def CountBetween(L,lower,upper):
    counter = 0

    for item in L:
        if item >=lower and item <= upper:
            counter = counter + 1

    return counter

def mainfunction():
    FSQs = GetFairSqures(999)
    print(FSQs)
    FILENAME = 'C-large-1.in'
    output = 'output.out'
    out = open(output,'w')
    f=open(FILENAME, 'r')
    NumberOfCases = int (f.readline())
    print(NumberOfCases)

    for i in range(1,NumberOfCases+1):
        Line = f.readline()
        Line =Line.strip('\n')
        lowerlimit = int(Line[:Line.find(' ')])
        upperlimit = int(Line[Line.find(' '):])
        outputline = 'Case #' + str(i)+ ': '
        outputline = outputline + str(CountBetween(FSQs,lowerlimit,upperlimit))
        outputline = outputline + '\n'
        out.write(outputline)
    out.close()

