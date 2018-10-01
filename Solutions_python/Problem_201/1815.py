from queue import PriorityQueue
from math import ceil
def bathroomStalls(N, K):
    q = PriorityQueue(maxsize=-1)
    q.put(-N)

    minimum, maximum = 0, 0
    while K > 0:
        K -= 1
        space = -q.get()
        spot = (space - 1) // 2

        minimum, maximum = spot, space - spot - 1
        q.put(-minimum)
        q.put(-maximum)

    return minimum, maximum

if __name__ == '__main__':

    T = int(input())
    for i in range(T):

        N, K = [int(x) for x in input().split()]

        minimum, maximum = bathroomStalls(N, K)
        print("Case #{}: {} {}".format(i + 1, maximum, minimum))
