__author__ = 'gena'

import numpy as np

np.intersect1d


def readMatrix(input, shape):
    arr = np.zeros(shape=shape)
    for i in range(shape[0]):
        arr[i] = np.array([int(a) for a in input.readline().split(" ")])
    return arr


def solve(filename):
    with open(filename) as f:
        T = int(f.readline())
        with open("solution", "w") as sol:
            for i in range(T):
                ans1 = int(f.readline()) - 1
                mat1 = readMatrix(f, (4, 4))
                ans2 = int(f.readline()) - 1
                mat2 = readMatrix(f, (4, 4))


                inters = np.intersect1d(mat1[ans1], mat2[ans2])
                if len(inters) == 1:
                   sol.write("Case #{0}: {1}\n".format(i + 1, int(inters[0])))
                elif len(inters) > 1:
                    sol.write("Case #{0}: {1}\n".format(i + 1, "Bad magician!"))
                elif len(inters) == 0:
                    sol.write("Case #{0}: {1}\n".format(i + 1, "Volunteer cheated!"))



solve("small")




