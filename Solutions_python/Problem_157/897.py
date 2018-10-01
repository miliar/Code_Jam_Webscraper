
d = { '1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
      'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
      'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
      'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'} }

def mul(a,b):
    res = d[a][b]
    if (len(res) == 2):
        return (-1, res[1])
    return (1, res[0])

def process(tc, arr):
    leftIdx = -1
    rightIdx = len(arr)
    leftMul = [1,'1']
    rightMul = [1,'1']
    success = False
    while leftIdx < rightIdx:
        leftIdx += 1
        while leftIdx < rightIdx:
            res = mul(leftMul[1],arr[leftIdx])
            leftMul[0] *= res[0]
            leftMul[1] = res[1]
            if (leftMul[0] == 1 and leftMul[1] == 'i'):
                break
            leftIdx += 1

        rightIdx -= 1
        while rightIdx > leftIdx:
            res = mul(arr[rightIdx],rightMul[1])
            rightMul[0] *= res[0]
            rightMul[1] = res[1]
            if (rightMul[0] == 1 and rightMul[1] == 'k'):
                break
            rightIdx -= 1


        i = leftIdx + 1
        midMul = [1,'1']
        while i < rightIdx:
            res = mul(midMul[1],arr[i])
            midMul[0] *= res[0]
            midMul[1] = res[1]
            i += 1

        if (midMul[0] == 1 and midMul[1] == 'j'):
            success = True
            break

    if success:
        print "Case #%d: YES" % tc
    else:
        print "Case #%d: NO" % tc


lines = [line.strip() for line in open('2/C-small-attempt0.in')]

n = int(lines[0])
for i in range(0, n):
    arr = lines[1+i*2].split(' ')
    L = int(arr[0])
    X = int(arr[1])
    s = ''
    for e in range(X):
        s += lines[1+i*2+1]
    process(i+1,s)

