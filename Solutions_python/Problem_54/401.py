def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a-b*int(a/b))

def pos(x):
    if x < 0:
        return -x
    else:
        return x

fin = open('B-large.in', 'r')
fout = open('B-large.out', 'w')

for c in range(int(fin.readline())):
    inputs = [int(i) for i in fin.readline().split(' ')]
    inputs.remove(inputs[0])

    #now inputs is the list of timings from each great event
    diffs = []
    for i in range(len(inputs)-1):
        diffs.append(pos(inputs[i] - inputs[i+1]))

    #now find gcd of the differences
    t = diffs[0]
    for j in diffs:
        t = gcd(t, j)

    #now find out the smallest number to add to each time
    ans = t - inputs[0]%t
    if ans == t:
        ans = 0
    print('Case #', c+1, ': ', ans, sep='', file=fout)

fin.close()
fout.close()
