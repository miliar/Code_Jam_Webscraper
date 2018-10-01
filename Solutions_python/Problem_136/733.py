
def solveB(file):
    data = ''
    resultTotal = []
    with open(file) as f:
        T = f.readline()
        T = int(T.strip())
        for index in xrange(T):
            data = f.readline()
            C,F,X = [float(val.strip()) for val in data.strip().split(' ')]
            
            rate = 2
            T1 = X / rate
            NumFarm = 0
            FarmTime = 0
            while True:
                T2 = FarmTime +  C/(rate) + X/(rate + F)
                if T2 < T1:
                    FarmTime = FarmTime + C/(rate)
                    NumFarm += 1
                    rate = rate + F
                    T1 = T2
                else:
                    break
            
            result = T2
            
            resultTotal.append(T1)
    

        with open('resultB.txt','w') as r:
            for index in xrange(len(resultTotal)):
                r.write('Case #{:}: {:0.7f} \n'.format(index + 1, resultTotal[index]))
