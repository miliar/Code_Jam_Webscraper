import time
from copy import deepcopy


print (time.ctime())

f_in = open('c:/temp/codejam/round2/b/B-small-attempt0.in')
f_out = open('c:/temp/codejam/round2/b/B-small-attempt0.out','w')

T = int(f_in.readline())
for case in range(1,T+1):

    P = int(f_in.readline())
    M_arr = [int(x) for x in f_in.readline().split()]
    prices = []
    for i in range(P):
        prices.append([int(x) for x in f_in.readline().split()])
    game_price = prices[0][0]
    must_buy = [[False for i in range(2**j)] for j in range(P-1,-1,-1)]
    for i in range(2**P):
        for j in range(P-M_arr[i]):
            k = i//(2**(P-j))
            must_buy[-1-j][k] = True
    count = 0
    for l in must_buy:
        count += l.count(True)
    
    res = count * game_price
    
    f_out.write('Case #' + str(case) + ': ' + str(res) + '\n')

f_out.close()
f_in.close()

print (time.ctime())

