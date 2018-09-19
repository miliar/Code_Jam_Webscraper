lines = open("A-small-attempt0.in").read().split("\n")
outp = open("output1.txt", "w")
caseCount = int(lines[0])
for k in range(caseCount):
    offset = 10 * k
    line1 = lines[offset + 2:offset + 6][int(lines[offset + 1])-1].split()
    line2 = lines[offset + 7:offset + 11][int(lines[offset + 6])-1].split()
    intersection = [val for val in line1 if val in line2]
    out="Case #%d: %s" % (k + 1, intersection[0] if len(intersection) == 1 else ["Volunteer cheated!", "Bad magician!"][len(intersection)>0])
    outp.write(out+"\n")
    k += 1
outp.flush()