f = open('tidy.in', 'r')
out = open('tidy.out', 'w')
f.readline()

test_case = 1
# brute force
def toList(x):
    return [int(a) for a in str(x)]

for l in f:
    N = int(l)
    largest = 0
    for i in range(1, N + 1):
        lp = toList(i)
        d = lp[0]
        pos = True
        for di in lp:
            if di < d:
                pos = False
                break
            if di > d:
                d = di
        if pos and i > largest:
            largest = i
    out.write('Case #{}: {}\n'.format(test_case, largest))
    test_case += 1
'''
for l in f:
    numlist = [int(x) for x in l[:-1]]
    ans = []
    if min(numlist) == 0:
        ans = [9] * (len(numlist) - 1)
    else:
        while len(numlist) != 0:
            if len(numlist) == 1:
                ans += numlist
                break
            elif numlist[0] < numlist[1]:
                ans += [numlist[0]]
                numlist = numlist[1:]
            elif numlist[0] == numlist[1]:
                l = 0
                while numlist[l] == numlist[0]: l += 1
            else:
                ans += [9] * (len(numlist) - 1)
                break
            numlist = numlist[1:]
    out.write('Case #{}: '.format(test_case))
    for d in ans:
        out.write('{}'.format(d))
    out.write('\n')
    test_case += 1
'''
