f = open("A-large.in", "r")
w = open("A-large.out", "w")
f.readline()
caseNo = 1
for line in f:
    data = line.split()[1]
    pool = int(data[0])
    ans = 0
    for num in range(1, len(data)):
        if int(num) > pool:
            ans += 1
            pool += 1
        pool += int(data[num])
    w.write("Case #" + str(caseNo) + ": " + str(ans) + '\n')
    caseNo += 1
w.close()
f.close()