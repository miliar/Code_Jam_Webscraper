import sys

cases = raw_input()
input = dict()

for i in range(int(cases)):
    input[i] = raw_input()

for i in input:
    count = 0
    sys.stdout.write("Case #")
    j = str(i + 1)
    sys.stdout.write(j)
    sys.stdout.write(": ")
    (a, b) = input[i].split()
    a = int(a)
    b = int(b)
    for n in range(a, b):
        modMul = str(a).__len__()
        for mul in range(1, modMul):
            k = n % (10**mul)
            m = k * (10 ** (modMul - mul)) + (n/10**mul)
            if m > n and m<=b:
                count += 1
    print count

