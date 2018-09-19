incoming = open('B-Large.in')
output = open('BLarge.out','w')
a = int(incoming.readline())

for i in range(1,a+1):
    x = incoming.readline().rstrip().split()
    N = int(x[0])
    S = int(x[1])
    p = int(x[2])
    success = 0
    for test in x[3:]:
        y = int(test)
        if (y+2)//3 >= p:
            success += 1
        elif (y+4)//3 >= p and S >=1 and y>=p:
            success += 1
            S -=1
    output.write("Case #%d: " % i)
    output.write(str(success) + '\n')
    
incoming.close()
output.close()
