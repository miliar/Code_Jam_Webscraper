import math


def assign_stalls(case):
    N = case['N']
    K = case['K']
    while K > 1:
        K -= 1
        N -= 1
        if K % 2 == 0:
            N = int(math.floor(N / 2))
        else:
            N = int(math.ceil(N / 2))
        K = int(math.ceil(K/2))
    return give_max_min(N)


def give_max_min(number: int):
    getal = (number-1)/2.0
    maxi = int(math.ceil(getal))
    mini = int(math.floor(getal))
    return str(maxi) + ' ' + str(mini)
