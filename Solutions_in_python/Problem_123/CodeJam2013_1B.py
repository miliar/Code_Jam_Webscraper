
f = open('A-large.in')
out = open('out.txt', 'w')

testNum = int(f.readline())
print('test number = ', testNum)

def HowManyMotosDoINeed(a, b):
    count = 0
    while a <= b:
         count += 1
         a += a - 1
    return (count, a)

def sol(armin, index):
    if (index < N):
        if (armin == 1):
            return N - index
        (insertsNum, grownA) = HowManyMotosDoINeed(armin, data[index])
        return min(N - index, insertsNum + sol(grownA + data[index], index + 1))
    else:
        return 0

for i in range (testNum):
    (A, N) = (int(x) for x in f.readline().split())
    data = [int(x) for x in f.readline().split()]
    # solve the problem
    data.sort()
    #print('A = ', A, 'data = ', data)



    opNum = sol(A, 0)

    print(' sol = ', opNum)
    out.write('Case #{0}: {1}\n'.format(i + 1, opNum))
           




    

