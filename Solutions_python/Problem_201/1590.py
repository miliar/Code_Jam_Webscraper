import math


def distribute(N, K):
    iteration = 0
    K0 = K
    K += 1
    while K > 1:
        K = K >> 1
        iteration += 1

    occupied = (1 << iteration) - 1
    N_rest = N - occupied
    K_rest = K0 - occupied

    space = 0
    while N_rest >= occupied + 1:
        space += 1
        N_rest -= occupied + 1

    number_of_large_spaces = N_rest

    if K_rest == 0:
        if number_of_large_spaces >= (occupied + 1)/2:
            return space + 1, space
        else:
            return space, space

    if K_rest <= number_of_large_spaces:
        return math.ceil(space / 2), math.floor(space / 2)

    else:
        return math.ceil((space - 1) / 2), math.floor((space - 1) / 2)


with open("C-small-2-attempt3.in", 'r') as input:
    lines = input.readlines()
    cases = lines[1:]

with open("output.txt", 'w') as output:
    index = 1
    for case in cases:
        N, K = case.split(" ")
        _max, _min = distribute(int(N), int(K))
        output.write("Case #{i}: {result}\n".format(i=index, result="{max} {min}".format(max=_max, min=_min)))
        index += 1
