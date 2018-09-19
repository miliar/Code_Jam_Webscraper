filein = open("PA.txt", "r")
out = open("PAout.txt", "w")
cases = int(filein.readline())
for i in xrange(cases):
    total = 0
    pos = 0
    ans1 = int(filein.readline())
    A = [[0] * 4 for j in xrange(4)]
    for j in xrange(4):
        A[j] = filein.readline().split()
    print A
    ans2 = int(filein.readline())
    B = [[0] * 4 for j in xrange(4)]
    for j in xrange(4):
        B[j] = filein.readline().split()
    print B
    for item in A[ans1-1]:
        if item in B[ans2-1]:
            pos = item
            total += 1
    if total > 1:
        out.write("Case #" + str(i+1) + ": " + "Bad magician!" + "\n")
    elif total == 1:
        out.write("Case #" + str(i+1) + ": " + pos + "\n")
    else:
        out.write("Case #" + str(i+1) + ": " + "Volunteer cheated!" + "\n")
        
