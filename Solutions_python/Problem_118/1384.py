import time, math

digitsA = []
A = 0
aex = False

digitsB = []
B = 0
bex = False

def makeSparseNum(s):
    # print "making sparse num out of >>",s,"<<"
    if s == "0": s = "1"
    num = []
    i = 0
    while i < len(s):
        if s[i] != "0":
            num.append(int(s[i]))
            num.append(0)
        else:
            num[len(num)-1] += 1
        i += 1
    return num

def printConstruct(n):
    s = ""
    for i in range(0, len(n)/2):
        s += str(n[i*2])
        for nulls in range(0, n[i*2 + 1]):
            s +="0"
    s += str(n[len(n) - 1])
    return s

def ininterval(digits, digitCount):
    global A, B, digitsA, digitsB
    if digitCount < digitsA or digitCount > digitsB:
        return False

    if digitCount > digitsA and digitCount < digitsB:
        return True

    # print "testing", digits, printConstruct(digits), "against", A, "and", B, ". digits:", digitCount, "vs", digitsA, digitsB

    #print "still testing", digits, "against", A, "and", B

    # check sparsenums
    if digitCount == digitsA:
        isBiggerThanA = False
        i = 0
        while(i < (len(digits) / 2.0)+ 1):
            if digits[i] > A[i]:
                isBiggerThanA = True
                break
            elif digits[i] < A[i]:
                break
            else: # digits equal, check zeros
                if len(digits) == i + 1:
                    # exactly equal
                    isBiggerThanA = aex
                    break
                if digits[i+1] < A[i+1]:
                    isBiggerThanA = True
                    break
                elif digits[i+1] > A[i+1]:
                    break
                else:
                    #equally many zeros, continue with next digit
                    pass
            i += 2

        if not isBiggerThanA:
            return False

    if digitCount == digitsB:
        isSmallerThanB = False
        i = 0
        while(i < len(digits) / 2.0 + 1):
            if digits[i] < B[i]:
                isSmallerThanB = True
                break
            elif digits[i] > B[i]:
                break
            else: # digits equal, check zeros
                if len(digits) == i + 1:
                    # exactly equal
                    isSmallerThanB = True #not bex
                    break
                if digits[i+1] > B[i+1]:
                    isSmallerThanB = True
                    break
                elif digits[i+1] < B[i+1]:
                    break
                else:
                    #equally many zeros, continue with next digit
                    pass
            i += 2
        return isSmallerThanB
    return True

def count(digits, currentDigitCount, adjustZero):
    zeroPositions = math.floor(len(digits) / 2)
    # print "counting",digits," zeroPos:", zeroPositions,"adjust0:",adjustZero
    if adjustZero > ((zeroPositions+1) // 2):
        return 0
    thiscount = 0
    maxNewZeros = (digitsB - currentDigitCount) 
    for zeros in range(0, maxNewZeros+1):
        # print "zeros:", zeros, "digits:", digits, "adjust: ", adjustZero
        newDigits = digits[:]
        newDigits[adjustZero * 2 - 1] += zeros
        newDigits[len(digits) - adjustZero * 2] = newDigits[adjustZero * 2 - 1] # might be the same entry
        newzeros = zeros * 2
        if len(digits) - adjustZero * 2 == adjustZero * 2 - 1:
            newzeros = zeros
        if ininterval(newDigits, currentDigitCount + newzeros):
            if (zeros > 0 or adjustZero == 1):
                thiscount += 1
                #print it for fun
                # print "fair:", printConstruct(newDigits)

            thiscount += count(newDigits, currentDigitCount + newzeros, adjustZero + 1)
    return thiscount

def isqrt(_x):
    # print "calculating isqrt of",_x,
    n = long(_x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2 ** (a+b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            if long(_x) == (x**2): 
                # print "exact!",
                return x, True
            # print "=",x
            return x, False
        x = y

def Solve(_A,_B):
    global A, B, digitsA, digitsB, aex, bex
    counter = 0
    _A, aex = isqrt(_A)
    _B, bex = isqrt(_B)
    A = makeSparseNum(str(_A))
    B = makeSparseNum(str(_B)) #math.floor(str(math.sqrt(long(_B)))))
    digitsA = len(str(_A))
    #print "len of", _A, ":", digitsA
    digitsB = len(str(_B))
    if ininterval([1], 1): 
        counter += 1
        # print "fair: 1"
    if ininterval([2], 1): 
        counter += 1
        # print "fair: 2"
    if ininterval([3], 1): 
        counter += 1
        # print "fair: 3"
    counter += count([2,0,1,0,2],3,1)
    counter += count([2,0,2],2,1)
    counter += count([1,0,2,0,1],3,1)
    # counter += count([2,0,1,0,2],3,1)#
    counter += count([1,0,1,0,2,0,1,0,1],5,1)
    for ones in range(2,10):
        digs = []
        for i in xrange(1, ones):
            digs.append(1)
            digs.append(0)
        digs.append(1)
        # print "dig:", digs, "ones:", ones
        counter += count(digs, ones, 1)
    return counter



start = time.time()
f = open('c.in')
T = int(f.readline())
for t in range(T):
    A,B = f.readline().split()
    result = Solve(A,B)
    print "Case #%d: %s" % (t+1, result)
elapsed = (time.time() - start)
print elapsed