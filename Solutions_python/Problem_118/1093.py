def isPalindrome(num):
    if num - int(num) != 0:
        return False
    num = str(int(num))
    l = len(num)
    for i in xrange(l):
        if num[i] != num[l-i-1]:
            return False
    return True

def allFairAndSquare(a, b):
    rtn = []
    for i in xrange(a, b+1):
        if isPalindrome(i) and isPalindrome(i**(0.5)):
            rtn.append(i)
    return rtn
    
f = open('C-small-attempt1.in', 'r')
g = open('output.txt', 'w')

n = int(f.readline())
count = 1
all = allFairAndSquare(1, 1000)

while count <= n:
    rng = f.readline().split()
    a, b = int(rng[0]), int(rng[1])
    
    x, y = 1000, 1000
    for i in xrange(len(all)):
        if all[i] >= a:
            x = i
            break
    
    for i in xrange(x, len(all)):
        if all[i] > b:
            y = i
            break
            
    total = 0
    if x == 1000:
        total = 0
    elif y == 1000:
        y = len(all)
        total = y-x
    else:
        total = y-x

    g.write("Case #" + str(count) + ": " + str(total) + '\n')
        
    count += 1
    
f.close()
g.close()