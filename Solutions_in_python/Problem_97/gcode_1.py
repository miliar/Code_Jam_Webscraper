freq = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'p', 'g', 'w', 'y', 'b', 'v', 'k', 'x', 'j', 'q', 'z']

def isRecyclable(initial, test, sentinel):
    if test < 10:
        return False

    strTest = str(test)

    val = strTest[0]
    repeated = True
    for char in strTest:
        repeated = repeated and char == val
        
    if repeated:
        return False
    
    testLen = len(strTest) - 1
    vals = []
    for i in xrange(0, testLen):
        pivot = testLen - i
        newStr = strTest[pivot:] + strTest[:pivot]
        if newStr[0] == '0':
            continue

        val = int(newStr)
        #print "TEST:{} VAL:{}".format(test, val)
        if val <= sentinel and val > test:
            #print "({}, {})".format(test, val)
            vals.append(val)

    if vals:
        return vals

    return False

def solve(first, second):
    test = first
    recycled = []
    for test in xrange(test, second):
        res = isRecyclable(first, test, second)
        if not res:
            continue
        for r in res:
            #print "({}, {})".format(test, r)
            recycled.append((test, r))

    return recycled


def read_file(path):
    with open(path, 'r') as f:
        num_cases = int(f.readline()[:-1])
        lines = []
        for index in xrange(num_cases):
            parts = [int(x) for x in f.readline()[:-1].split(' ') if x ]
            recycled = solve(parts[0], parts[1])
            #print "COUNT: {}\n{}".format(len(recycled), recycled)
            #print "\n"
            print "Case #{}: {}".format(index+1, len(recycled))


if __name__ == '__main__':
    import sys
    read_file(sys.argv[1])
