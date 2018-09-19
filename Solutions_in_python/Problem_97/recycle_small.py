def numOfDigits(x):
    m = 10
    n = 1
    while x > m:
        m *= 10
        n += 1
    return n
        
def rotateInt(x,numDigits):
    m = pow(10,numDigits-1)
    d = x / m
    r = x % m
    return r * 10 + d
    

ifile = 'C-small-attempt0.in'
ofile = 'C-small-attempt0.out'

ifptr = open(ifile)
ofptr = open(ofile,'w')

N = int(ifptr.readline().rstrip()) #No. of test cases

for i in range(0,N):
    
    nums = [int(x) for x in ifptr.readline().rstrip().split()]
    
    A = nums[0]
    B = nums[1]
    
    result = 0
    
    for n in range(A,B):
        d = numOfDigits(n)
        z = n
        for k in range(0,d-1):
            z = rotateInt(z,d)
            if z > n and z >= A and z <= B:
                #print "%d <> %d" % (n, z)
                result += 1
    
    ofptr.write("Case #%d: %d\n" % (i+1,result))

ifptr.close()
ofptr.close()