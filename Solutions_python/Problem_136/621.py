# Python 3.2

from common import *

def main(casenum):
    c, f, x = readfloats()

    # rate = 2.0
    # farms = 0
# 
    # best = x / rate
    # farm_time = 0
# 
    # while True:
        # farm_time += c / rate
        # farms += 1
        # rate += f
# 
        # cur = farm_time + (x / rate)
# 
        # if cur <= best:
            # best = cur
        # else:
            # break


    rate = 2.0
    farm_time = 0
    num_farms = int((x / c) - (2.0 / f))

    print (num_farms)
    for i in range(num_farms):
        farm_time += c / rate
        rate += f

    writeline('Case #{}: {}'.format(casenum, farm_time + (x / rate)))

run(main)
