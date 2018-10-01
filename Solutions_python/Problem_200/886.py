def ltoI(number):
    return int(''.join(str(i) for i in number))

import sys
T = sys.stdin.readline()
for k, line in enumerate(sys.stdin):
    n = list(line[0:-1])
    for i in range(len(n)-1, 0, -1):
        if int(n[i]) < int(n[i-1]):
            n[i] = 9
            n[i-1] = int(n[i-1]) - 1
            for j in range(i+1, len(n)):
                n[j] = 9


    print("CASE #{}: {}".format(k+1, ltoI(n)))

    if T == k+1:
        break
