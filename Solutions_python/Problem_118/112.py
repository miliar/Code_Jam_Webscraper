MAX_DIGITS = 26
fslist = []

def getnum(a, digits, odd):
    ret = 0
    if odd:
        for i in range(digits):
            ret = ret * 10 + a[i]
        for i in range(digits - 2, -1, -1):
            ret = ret * 10 + a[i]
    else:
        for i in range(digits):
            ret = ret * 10 + a[i]
        for i in range(digits - 1, -1, -1):
            ret = ret * 10 + a[i]
    return ret
    
def dfs(number, leftsum, mid ,digits):
    if digits > MAX_DIGITS or leftsum * 2 + mid >= 10:
        return

    if leftsum * 2 + mid < 10:
        fslist.append(getnum(number, digits, True))
    
    if leftsum * 2 + mid * 2 < 10:
        fslist.append(getnum(number, digits, False))
        
    for i in xrange(0, 4):
        if digits == 0 and i == 0:
            continue
        number[digits] = i
        dfs(number, leftsum + mid, i * i, digits + 1)

a = [0 for i in xrange(5 + MAX_DIGITS)]
dfs(a, 0, 0, 0)
fslist.sort()
for i in xrange(len(fslist)):
    fslist[i] = fslist[i] * fslist[i]
print fslist[1:41]
print len(str(fslist[-1]))
print len(fslist)

fin = open("in.txt")
fout = open("C.out", "w")
T = int(fin.readline().strip())
cas = 0

import bisect
while T > 0:
    line = fin.readline()
    if line.strip() == '':
        continue
    T -= 1
    parts = line.split()
    A = int(parts[0])
    B = int(parts[1])
    if cas < 10:
        print A, B
        print bisect.bisect_right(fslist, B), bisect.bisect_left(fslist, A)
    ret = bisect.bisect_right(fslist, B) - bisect.bisect_left(fslist, A)
    cas += 1
    fout.write("Case #%d: %d\n" % (cas, ret))
