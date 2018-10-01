def chkpalin(num):
    temp = num
    rev = 0
    while temp > 0:
        ld = temp % 10
        rev = rev*10 + ld
        temp = temp/10
    if rev == num :
        return True
    else:
        return False

def chksqr(num):
    if num == 1:
        return True, 1
    for i in range(num):
        if i**2 == num:
            return True, i
    return False, 0

def fairnsqr(A,B):
    count = 0
    for i in range(A,B+1):
        if chkpalin(i) == True:
            a, b = chksqr(i)
            if a == True and chkpalin(b) == True:
                count += 1
    return count

def runprog(FILE):
    infile = open(FILE)
    line1 = infile.readline()
    T = int(line1.strip('\n'))
    for i in range(T):
        line2 = infile.readline()
        arr = (line2.strip('\n')).split(' ')
        solution = fairnsqr(int(arr[0]),int(arr[1]))
        print 'Case #' + str(i+1) + ': ' + str(solution)
