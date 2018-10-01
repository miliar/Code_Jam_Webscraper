with open('B-large.in', 'r') as f:
    lines = f.readlines()

t = lines[0]
examples = lines[1:]
nums = [[int(n) for n in num.strip()] for num in examples]


def initZeroNum(num):
    return [0 for n in num]


def isInRange(candidate, topRange):
    i = 0

    while i < len(topRange):
        if candidate[i] < topRange[i]:
            return True
        elif candidate[i] > topRange[i]:
            return False
        else:
            i += 1
    return True


def isTidy(num):
    a = num[0]
    for b in num[1:]:
        if b < a:
            return False
        else:
            a = b
    return True


def removeOne(num):
    def removeOneIndex(num, i):
        if num[i] > 0:
            num[i] = num[i] - 1
            return num
        elif i == 0:
            return None
        else:
            num[i] = 9
            return removeOneIndex(num, i - 1)

    newNum = removeOneIndex(num, len(num) - 1)
    if newNum and len(newNum) > 1:
        for i in xrange(len(newNum) - 1):
            first = i
            second = i + 1
            if newNum[first] > newNum[second]:
                newNum[first] = newNum[first] - 1
                for z in xrange(second, len(newNum)):
                    newNum[z] = 9
    return newNum


def bumpNum(num):
    carry = 1
    for i in xrange(0, len(num)):
        ii = len(num) - 1 - i
        current_num = num[ii] + carry
        carry = 0
        if current_num > 9:
            num[ii] = 0
            carry = 1
        else:
            num[ii] = current_num
            for i in xrange(0, len(num) - 1):
                ii = len(num) - 1 - i
                ii2 = len(num) - 2 - i
                if num[ii] < num[ii2]:
                    num[ii] = num[ii2]
            return num

    return None


def findTidy(num):
    candidate = [n for n in num]
    # print 'Calculating', num
    while candidate is not None and isInRange(candidate, num):
        if isTidy(candidate):
            # print 'found', candidate
            return candidate
        candidate = removeOne(candidate)
        # print candidate
    return None

tidys = [findTidy(n) for n in nums]


def calculateStrWithoutPadding(num):
    sawNonZero = False
    out = ''
    for n in num:
        if sawNonZero or n != 0:
            sawNonZero = True
        if sawNonZero:
            out += str(n)
    return out


for i in xrange(1, len(tidys) + 1):
    print 'Case #{}: {}'.format(i, ''.join(
        calculateStrWithoutPadding(tidys[i - 1])))
