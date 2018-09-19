import math

def inc(n):
    result = n[:]
    index = len(n) - 1

    if result[index] is 9:
        if index is 0:
            result[index] = 0
            result.insert(0, 1)
        else:
            result = inc(result[:index]) + [0]
    else:
        result[index] = result[index] + 1

    return result


def nextPalindrome(n):
    magic = lambda nums: int(''.join(str(i) for i in nums))
    
    t = list(map(int, str(n)))
    
    length = len(t)

    middle = length // 2

    if length % 2 is 0:
        tmp = inc(t[:middle])
        pre = tmp[:]
        post = tmp[:]
        post.reverse()
        result = pre + post
        
    else:
        tmp = inc(t[:middle + 1])
        
        pre = tmp[:]
        post = tmp[:len(tmp) - 1]
        post.reverse()
        result = pre + post

    if len(result) > length:
        del result[middle + 1]
    
    return magic(result)

def isPalindrome(n):
    n = str(n)
    if len(n) < 2:
        return True
    if n[0] != n[-1]:
        return False
    return isPalindrome(n[1:-2])


def makePalindrome(n):
    magic = lambda nums: int(''.join(str(i) for i in nums))
    
    t = list(map(int, str(n)))
    
    if isPalindrome(n):
        return n

    else:
        length = len(t)
        middle = length // 2

        if length % 2 is 0:
            tmp = t[:middle]
            pre = tmp[:]
            post = tmp[:]
            post.reverse()
            
            if post > t[middle:]:
                result = pre + post

            else:
                tmp = inc(t[:middle])
                pre = tmp
                post = tmp
                post.reverse()
                result = pre + post
                result = pre + post

        else:
            tmp = t[:middle]
            pre = tmp[:]
            post = tmp[:]
            post.reverse()

            if post > t[middle + 1:]:
                pre.append(t[middle + 1])
                result = pre + post

            else:
                tmp = inc(t[:middle + 1])
                pre = tmp[:]
                post = tmp[:len(tmp) - 1]
                post.reverse()
                result = pre + post

        if len(result) > length:
            del result[middle + 1]

    return magic(result)


inFileName = input()
outFileName = "result.out"

inFile = open(inFileName, 'r')
outFile = open(outFileName, 'w')

numTest = inFile.readline().strip()

print(numTest)

for i in range(int(numTest)):
    A, B = inFile.readline().strip().split(' ')
    A = int(A)
    B = int(B)

    count = 0
    a = math.sqrt(A)
    p = makePalindrome(int(a))
    pp = p*p
    
    if A <= pp <= B and isPalindrome(pp):
            count += 1

    p = nextPalindrome(p)
    pp = p*p

    while(A <= pp <= B):
        if isPalindrome(pp):
            count += 1

        p = nextPalindrome(p)
        pp = p*p

    result = "Case #" + str(i + 1) + ": " + str(count)

    print(result)
    outFile.write(result + "\n")

inFile.close()
outFile.close()
