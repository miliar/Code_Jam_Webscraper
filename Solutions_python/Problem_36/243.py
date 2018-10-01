from itertools import izip, count
outFile = open("out.out", "w")
case = 1
phrase = "welcome to code jam"
firstLine = True
for line in open("C-small-attempt1.in","U"):
    if firstLine:
        firstLine = False
        continue
    st = line.strip()
    seqCount = []
    seqCount.append([])
    for pc in phrase:
        seqCount[0].append(0)
    for ind, c in enumerate(st):
        # print c
        seqCount.append([])
        for i, pc, n in izip(count(), phrase, seqCount[ind]):
            seqCount[ind + 1].append(n)
            if c == pc:
                if i == 0:
                    seqCount[ind+1][i] += 1
                else:
                    seqCount[ind+1][i] += seqCount[ind][i - 1]
                seqCount[ind+1][i] %= 1000
    output = "Case #%d: %04d\n" % (case, seqCount[-1][-1])
    # print output
    outFile.write(output)
    case += 1
outFile.close()
