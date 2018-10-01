import math
t = int(input())  
for i in range(1, t + 1):
    n, k = [int(val) for val in input().split()] 

    close2 = int(math.log(k, 2))
    groupN = int(math.pow(2, close2))
    freeN = n - (groupN - 1)
    groupS = freeN // groupN
    biggerGN = freeN - groupN * groupS 
    difff = biggerGN - (k - groupN)
    #print(groupN, freeN, groupS, biggerGN, difff)

    if difff > 0:
        groupS += 1
    groupS -= 1
    
    res2 = groupS // 2
    res1 = res2 + groupS % 2
    print("Case #{}: {} {}".format(i, res1, res2))
