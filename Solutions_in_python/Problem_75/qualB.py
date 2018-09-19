import sys

def combine(ele):
    e = ele.pop()
    if len(ele) != 0:
        lele = ele[-1]
        for c in C:
            if (lele == c[0] and e == c[1]) or (lele == c[1] and e == c[0]):
                ele.pop()
                ele.append(c[2])
                return combine(ele)
    ele.append(e)
    return ele
def destroy(ele):
    if len(ele) > 1:
        for i in range(0, len(ele)-1):
            eis = ele[i:]
            for j in range(1, len(eis)):
                ei = eis[0]
                ej = eis[j]
                for d in D:
                    if (ei == d[0] and ej == d[1]) or (ei == d[1] and ej == d[0]):
                        ele = []
                        return []
    return ele

inf = open('B-large.in', 'r')
outf = open('B-large.out', 'w')

T = int(inf.readline())
for t in range(1,T+1):
    line = inf.readline().rstrip().split(' ')

    i = 0
    Cn = int(line[i])
    C = line[i+1:i+1+Cn]
    for c in C:
        c = c.split()
    i += Cn + 1

    Dn = int(line[i])
    D = line[i+1:i+1+Dn]
    for d in D:
        d = d.split()
    i += Dn + 1

    Nn = int(line[i])
    N = line[i+1]

    ele = []
    for e in N:
        ele.append(e)
        ele = combine(ele)
        ele = destroy(ele)
        #print ele
    sys.stdout.write("Case #" + str(t) + ": ")
    print ele
    outf.write("Case #" + str(t) + ": [")
    st = ""
    for e in ele:
        st = st + e + ", "
    if len(ele) == 0:
        st = "]\n"
    else:
        st = st[:-2] + "]\n"
    outf.write(st)
outf.close()
inf.close()
