INPUT_FILE_NAME = 'B-large.in'
OUTPUT_FILE_NAME = 'out'

fin = open(INPUT_FILE_NAME)
fout = open(OUTPUT_FILE_NAME, 'w')

def f(n):
    a = list(n)
    for i in range(len(a)):
        a[i] = int(a[i])
    for i in range(len(a) - 2, -1, -1):
        if a[i] > a[i + 1]:
            a[i] -= 1
            if a[i] < 0:
                a[i] = 9
            for j in range(i + 1, len(a)):
                a[j] = 9
    res = 0
    for i in range(len(a)):
        res = res * 10 + a[i]
    return res

for case in xrange(1, 1 + int(fin.readline())):
    n = fin.readline().strip()
    fout.write("Case #{0}: {1}\n".format(case, f(n)))

fout.close()
fin.close()
