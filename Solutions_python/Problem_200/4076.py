def findTindy(num):
    x = num
    while not isTindy(x):
        x -= pminus(x);
    return x

def isTindy(num):
    return sorted(list(str(num))) == list(str(num))

def pminus(num):
    numList = list()
    x = list(str(num))
    while len(x) >= 2:
        if int(x[-2]) > int(x[-1]):
            numList.insert(0, x[-1])
            break
        elif int(x[-2]) == int(x[-1]):
            numList.insert(0, '0')
        else:
            numList.insert(0, x[-1])
        x = x[:-1]
    return list2Num(numList) + 1

def list2Num(numList):
    s = ''.join(numList)
    s = int(s)
    return s

def main():
    case = int(input())
    for i in range(case):
        x = int(input())
        print('Case #{0}: {1}'.format(i+1, findTindy(x)))


if __name__ == '__main__':
    main()