import math
from decimal import *
N_questions = input()

def l_product(plist):
    p = 1
    for i in plist:
        p *= i
    return p

getcontext().prec = 40

for q_num in range(int(N_questions)):
    n,k = list(map(int,input().split()))
    u = Decimal(input())*10000
    probabilities = list(map(lambda x: Decimal(x)*10000,input().split()))
    probabilities.append(10000)

    probabilities.sort() # sort probabilites from lowest to highest

    for i in range(n):
        if u == 0:
            break
        added_amount = probabilities[i+1] - probabilities[i]
        if added_amount*(i+1) <= u:
            for j in range(i+1):
                probabilities[j] += added_amount
                u -= added_amount
        else:
            for j in range(i+1):
                probabilities[j] += u/(i+1)
            u = 0
            break

    # if q_num + 1 == 6:
    #     print(probabilities, product(probabilities) * 10000**(-n-1))

    solution = l_product(probabilities) * Decimal(10000**(-n-1))

    # probabilities = [ p/10000 for p in probabilities]
    # # print(probabilities, product(probabilities))
    # solution = product(probabilities)

    print("Case #{}: {:.6f}".format(q_num + 1, min(solution,1) ))

