inp = open('B-large.in', 'r+')
out = open('output', 'r+')

t = int(inp.readline()) # number of test cases

for i in range(t):
    tokens = inp.readline().split(" ")
    ints = [int(x) for x in tokens]
    spotential = 0
    count = 0

    n = ints.pop(0) # number of googlers
    s = ints.pop(0) # number of surprises
    p = ints.pop(0) # score to compare

    diffs = [(x - p*3) for x in ints]

    for d in diffs:
        if p > 1:
            if d > -3:
                count += 1
            elif d > -5:
                spotential += 1
        elif p is 1:
            if d is -2:
                count += 1
            elif d > -2:
                count += 1
        elif p is 0:
            count = n
            spotential = 0
            break
    
    count += min(spotential, s)
        
    out.write("Case #" + str(i+1) + ": " + str(count) + "\n")