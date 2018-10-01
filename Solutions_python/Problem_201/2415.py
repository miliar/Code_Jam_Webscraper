def next_spot(occupied, ls, rs):
    possible = set()
    best = -1

    for i in range(1, len(occupied) - 1):
        if occupied[i] == False:
            cur = min(ls[i], rs[i])

            if cur > best:
                possible = set()
                possible.add(i)

                best = cur

            elif cur == best:
                possible.add(i)

    if len(possible) == 1:
        return possible.pop()

    best = -1
    next_possible = set()

    for p in possible:
        cur = max(ls[p], rs[p])

        if cur > best:
            next_possible = set()
            next_possible.add(p)

            best = cur

        elif cur == best:
            next_possible.add(p)
    
    return min(next_possible)



def stalls(n, k):
    occupied = [False for i in range(n + 2)]
    occupied[0] = True
    occupied[-1] = True

    ls = [i-1 for i in range(n + 2)]
    rs = [n - i for i in range(n + 2)]

    for p in range(k):

        spot = next_spot(occupied, ls, rs)

        # if last then return
        if p == k - 1:
            return (max(ls[spot], rs[spot]), min(ls[spot], rs[spot]))

        occupied[spot] = True

        # update ls and rs

        temp = 0
        # setting ls
        for i in range(spot+1, n+2):
            if occupied[i] == True:
                break

            ls[i] = temp
            temp += 1

        temp = 0
        # setting rs
        for i in range(spot-1, 0, -1):
            if occupied[i] == True:
                break

            rs[i] = temp
            temp += 1



# print("Case #{}: {} {}".format(1, *stalls(4, 2)))

t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

    print("Case #{}: {} {}".format(i, *stalls(n, k)))




# # check out .format's specification for more formatting options
