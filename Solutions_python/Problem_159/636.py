def case1(rounds):
    eaten = 0
    for i in range(len(rounds)-1):
        r1 = rounds[i]
        r2 = rounds[i+1]
        if r1 > r2:
            eaten += abs(r1 - r2)
    return eaten

def case2(rounds):
    # determine rate
    rate = 0
    for i in range(len(rounds)-1):
        r = rounds[i] - rounds[i+1]
        if r > rate:
            rate = r

    #print("Determined rate of %d" % rate)
    eaten = 0
    for i in range (len(rounds)-1):
        rnd = rounds[i]
        if rnd <= rate:
            #print(rnd)
            eaten += rnd

        else:
            #print(rate)
            eaten += rate

    return eaten
        
inp = """INPUT_HERE""".split('\n')

T = int(inp[0])
problems = []
case = 1
for i in range(2, 2 * T + 1, 2):
    prob = [int(j) for j in inp[i].split()]
    #print(prob)
    print("Case #%d: %d %d" % (case, case1(prob), case2(prob)))
    case += 1



























