import sys
#import argpase

import numpy as np 


def friendsneeded(shynessfrequency):
    npshy = np.array( [int(c) for c in shynessfrequency] )
    npshycum = npshy.cumsum()
    pplstanding = npshycum[0]
    additional = 0
    for i in range(len(npshy))[1:]:
        pplstanding = npshycum[i-1]+additional
        if i>pplstanding:
            additional += i - pplstanding
    return additional


if "__main__" == __name__:
    
    print(sys.argv[1])
    inputfile = sys.argv[1]

    with open(inputfile, 'r') as f:
        T = int(f.readline())
        shynesses = []
        for _ in range(T):
            shynesses.append(f.readline().split()[1])
    out = ""

    for i in range(T):
        out += "Case #{}: {}\n".format(i+1, friendsneeded(shynesses[i]))

    with open("out_"+inputfile, 'w') as f:
        f.write(out)
    print(out)