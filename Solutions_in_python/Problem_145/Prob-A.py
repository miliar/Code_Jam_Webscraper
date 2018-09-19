import sys
from math import sqrt, floor, log2
f = open(sys.argv[1], 'r')

numOfTest = int(f.readline())

for i in range(1, numOfTest + 1) :
    print("Case #" + str(i) + ":", end=' ')
    
    # read test case
    temp = f.readline().split('/')
    p = int(temp[0])
    q = int(temp[1])

    if log2(q) != int(log2(q)):
        print("impossible")
        continue
    ans = 1
    while True:
        if p * 2 >= q:
            break
        else :
            ans += 1
            q /= 2
    print(ans)
