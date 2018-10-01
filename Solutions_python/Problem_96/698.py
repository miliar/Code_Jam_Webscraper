f = open("B-large.in", 'r')
allfile = f.read()
lines = allfile.split("\n")
numMax = []
for x in xrange(1,len(lines)-1):
    nums = lines[x].split(" ")
    N = int(nums[0])
    S = int(nums[1])
    p = int(nums[2])
    numBothGreater = 0
    numOneGreater = 0
    for y in xrange(3,len(nums)):
        num = int(nums[y])
        if num % 3 == 0:
            if num/3 >= p:
                numBothGreater += 1
            elif num/3 + 1 >= p and num > 0 and num < 30:
                numOneGreater += 1
        elif num % 3 == 1:
            if num/3 + 1 >= p:
                numBothGreater += 1
        elif num % 3 == 2:
            if num/3 + 1 >= p:
                numBothGreater += 1
            elif num/3 + 2 >= p:
                numOneGreater += 1
    numMax.append(numBothGreater + min(numOneGreater, S))
f = open("problem2.out", 'w')
for x in xrange(len(numMax)):
    f.write("Case #" + str(x+1) + ": " + str(numMax[x]) + "\n")
