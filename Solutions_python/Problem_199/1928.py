inp = open("pancakes.in", 'r')
opt = open("pancakes.out", 'w')

l = []
Ks = []
T = None
for line in inp:
    if T is None:
        T = int(line)
    else:
        li = line.split(" ")
        l.append(li[0])
        Ks.append(int(li[1]))

# go from left and right sides, flipping K whenever a - is found
# either all pancakes will end up +, or we will get to a situation where the left number is K away from the right number

for x in range(len(l)):
    case = l[x]
    ileft = 0
    iright = len(case)-1
    flips = 0
    # let's try for now without deepcopy
    while case != "+"*len(case):
        ileft = case.find('-', ileft, iright+1)
        iright = case.rfind('-', ileft, iright+1)
        if iright - ileft < Ks[x]-1:
            break
        copy = list(case)
        # do leftmost part
        for c in range(ileft,ileft+Ks[x]):
            copy[c] = '+' if copy[c] == '-' else '-'
        flips += 1
        # flip rightmost part
        if iright-ileft > Ks[x]-1:
            for c in range(iright-Ks[x]+1,iright+1):
                copy[c] = '+' if copy[c] == '-' else '-'
            flips += 1
        case = "".join(copy)
        #case = ""
        #for ch in copy:
        #    case += ch
    if case == "+"*len(case):
        opt.write("Case #" +str(x+1) + ": " + str(flips) + "\n")
    else:
        opt.write("Case #" +str(x+1) + ": IMPOSSIBLE\n")

opt.close()
