happyMap = {2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{},10:{}} # for each base store numbers happy in it

def makeDigits(num, base):
    digits = []
    while num >= base:
        digits.append(num % base)
        num = num / base
    digits.append(num)

    return digits

def digitsHappy(digits, base, usedNum = {}):
    num = 0
    for n in digits:
        num += n*n
        
    if num in happyMap[base]: return happyMap[base][num]

    if num in usedNum:
        happyMap[base][num] = False
        return False
    usedNum[num] = True
    if num == 1:
        return True
    
    newDigits = makeDigits(num, base)
    isHappy = digitsHappy(newDigits, base, usedNum)
    happyMap[base][num] = isHappy
    return isHappy

def numHappy(num, base):
    if num in happyMap[base]: return happyMap[base][num]
    return digitsHappy(makeDigits(num,base), base, {})

f = open("indata.txt")
of = open("outdata.txt",'w')
numTests = int(f.readline())

for i in range(0,numTests):
    line = f.readline()
    bases = [int(x) for x in line.split(" ")]
    smallest = 0
    for j in range(2,10000000):
        allGood = True
        for base in bases:
            if not numHappy(j,base):
                allGood = False
        if allGood: break
    print i, j
    of.write("Case #%d: %d\n" % (i+1,j))

f.close()
of.flush()
of.close()


