fname = "A-large.in"


def caseWritten(num, string):
    return "Case #" + str(num+1) + ": " + string + "\n"

def WireCross(wires, n):
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            #print wires[i], wires[j]
            if wires[i][0] < wires[j][0] and wires[i][1] > wires[j][1]:
                count += 1
            elif wires[i][0] > wires[j][0] and wires[i][1] < wires[j][1]:
                count += 1
    return count

f = open(fname)
case = int(f.readline())
string = ''
for ca in range(case):
    in_put = f.readline().rstrip("\n").split()
    lines = int(in_put[0])
    wires = []
    for li in range(lines):
        input1 = f.readline().rstrip("\n").split()
        wires.append([int(input1[0]), int(input1[1])])
    #print wires
    count = WireCross(wires, lines)
    newString = str(count)
    string += caseWritten(ca, newString)


dot = fname.find(".")
oname = fname[:dot] + "-o" + fname[dot:]
o = open(oname, 'w')
o.write(string)
o.close()
print "fin"
