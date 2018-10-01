import sys
fileName = 'magicka_test'
f = open(fileName + '.in')
outFile = open(fileName +'.out', 'w')
def println(s):
    print >> outFile, s
    print s

testCases = int(f.readline())
for t in range(testCases):
    data = f.readline().split()
    c = int(data[0])
    combos = {}
    opposed = set()
    for i in range(c):
        z = data[1+i]
        if z[0] < z[1]: combos[z[:2]] = z[2]
        else:
            combos[z[1]+z[0]] = z[2] 
    index = c + 1
    d = int(data[index])
    for i in range(d):
        opposed.add(data[index + 1 +i])
    index += 1 + d
    n = int(data[index])
    input = data[index+1]
    seq = []
    for s in input:
        if len(seq) == 0: seq.append(s) 
        else:
            # combine
            if s < seq[-1]: z = s + seq[-1]
            else: z = seq[-1] + s
            p = combos.get(z, None)
            if p: seq[-1] = p
            else:
                # opposed?
                clear = False
                for w in seq: clear |= (w+s) in opposed or (s+w) in opposed
                if clear:
                    seq = []
                else:
                    seq.append(s)
    println('Case #%d: [%s]' % (t + 1, ', '.join(seq)))