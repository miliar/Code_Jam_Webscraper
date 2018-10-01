
import math

t = int(input())  # read a line with a single integer
for m in range(1, t + 1):
    n, p = [int(s) for s in input().split(" ")]
    needed = [int(s) for s in input().split(" ")]

    ingredients = []
    for j in range(n):
        ingredients.append(sorted([int(s) for s in input().split(" ")]))

    count = 0

    index = [0] * n
    # print (ingredients)

    while max(index) < p:
        gmin = 0
        gmax = 1e10
        valid = True
        max_index = 0
        # print (index)
        for ing in range(n):
            i = index[ing]
            loc_min = ingredients[ing][i] / (needed[ing] * 1.1)
            loc_max = ingredients[ing][i] / (needed[ing] * 0.9)

            if math.ceil(loc_min) > math.floor(loc_max):
                # print("fail0")
                index[ing] += 1
                break
            if math.ceil(loc_min) > math.floor(gmax):
                # print ("fail1", loc_min, gmax)
                index[max_index] += 1
                break

            if math.floor(loc_max) < math.ceil(gmin):
                # print ("fail2", loc_max, gmin)
                index[ing] += 1
                break

            gmin = loc_min if loc_min > gmin else gmin

            if loc_min < gmax:
                gmax = loc_max
                max_index = ing

            if ing == n - 1:
                index = [l + 1 for l in index]
                count += 1

    print("Case #{}: {}".format(m, count))
