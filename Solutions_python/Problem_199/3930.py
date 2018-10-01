import sys


def flip(cakes, flips, test_num, flip_size):
    #print(flips, cakes,flip_size)
    if len(cakes) < flip_size:
        print("Case #{}: {}".format(test_num, "IMPOSSIBLE"))
        return
    if len(cakes) == flip_size:
        sign = cakes[len(cakes)-1]
        #print("sign:",sign,flip_size)
        for current in cakes:
            #print("current:",current)
            if sign != current:
                print("Case #{}: {}".format(test_num, "IMPOSSIBLE"))
                return


    #this_flip_size = min(len(cakes),flip_size )
    #print(this_flip_size)

    for c in range(1, flip_size+1):
        #print("flip ",c,  cakes[len(cakes) - c])
        if cakes[len(cakes) - c] == '+':
            cakes[len(cakes) - c] = '-'
        else:
            cakes[len(cakes) - c] = '+'

    # print("flipped cakes", cakes)
    found_minus = 0
    while len(cakes) > 0 and found_minus == 0:
        #print("last cake",cakes[len(cakes)-1])
        if cakes[len(cakes) - 1] == '+':
            cakes.pop()
        else:
            found_minus = 1

    if len(cakes) > 0 and flips < 10:
        #print('deeper')
        flip(cakes, flips + 1, test_num, flip_size)
    else:
        print("Case #{}: {}".format(test_num, flips + 1))
        return


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    stuff = sys.stdin.readline().rstrip('\n')
    # print(str(stuff))
    start_cakes = list(stuff.split(" ")[0])
    flipper_size = int(stuff.split(" ")[1])

    #print("start:", i, start_cakes, flipper_size)

    found_minus = 0
    while len(start_cakes) > 0 and found_minus == 0:
        if start_cakes[len(start_cakes) - 1] == '+':
            start_cakes.pop()
        else:
            found_minus = 1

    if len(start_cakes) > 0:
        flip(start_cakes, 0, i, flipper_size)
    else:
        print("Case #{}: {}".format(i, 0))
