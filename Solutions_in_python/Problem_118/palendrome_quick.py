#import gmpy
#import math

def isFair(number):
    if isinstance(number, int):
        number = str(number)
    return (number == number[::-1])
    
#def isSquare(number):
#    if isinstance(number, basestring):
#        number = int(number)
#    return gmpy.is_square(number)

fairList = [1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004]

f = open('C-large-1.in', 'r')

# read first line, number of trials
trials = int(f.readline())
for i in range(trials):
    nums = [int(x) for x in f.readline().strip().split()]
    begin = nums[0]
    end = nums[1]
    fairsGreater = [x for x in fairList if x >= begin]
    fairsWithin = [x for x in fairsGreater if x <= end]
#    beginRoot = int(math.ceil(math.sqrt(begin)))
#    endRoot = int(math.sqrt(end))
#    for j in range(beginRoot, endRoot + 1):
#        if isFair(j) and isFair(j*j):
#            print str(j*j)
#            fairCount += 1
    print 'Case #' + str(i + 1) + ': ' + str(len(fairsWithin))