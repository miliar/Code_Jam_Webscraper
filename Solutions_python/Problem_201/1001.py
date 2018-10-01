import math
f = open("C-small-2-attempt0.in","r")
data = []
for line in f:
    data.append(line.strip().split(" "))
f.close()
for i in range(1,len(data)):
    N = int(data[i][0])
    K = int(data[i][1])
    floor = int(math.log(K) / math.log(2))
    subSum = N - 2**floor + 1
    count = 2**floor
    number1 = subSum // count
    number2 = number1 + 1
    Nnumber2 = subSum - number1 * count
    Nnumber1 = count - Nnumber2
    position = K - 2**floor + 1
    if position <= Nnumber2:
        Max = number2 // 2
        Min = number2 - 1 - Max
    else:
        Max = number1 // 2
        Min = number1 - 1 -Max
    print ("Case #"+str(i)+": "+str(Max)+" "+str(Min))
        
    
