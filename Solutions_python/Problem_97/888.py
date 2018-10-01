f = open("cinput.txt")

c = 0

for line in f:
    if c == 0:
        c += 1
        continue
    r = 0
    r_list = []
    pairs = []
    A = int(line.split(" ")[0])
    B = int(line.split(" ")[1])
    if A < 10:
        print "Case #" + str(c) + ": 0"
    for i in range(A, B+1):
        si = str(i)
        for j in range(len(si)-1):
            new = si[len(si)-(j+1):]
            new += si[:len(si)-(j+1)]
            if (int(new) > i) and (int(new) <= B):
                pair = (i,new)
                if pairs != []:
                    if pairs.count(pair) > 0:
                        continue
                r_list.append(int(new))
                pairs.append(pair)
    r_list.sort()
    r_count = 0
    print "Case #" + str(c) + ": " + str(len(r_list))
    c += 1
