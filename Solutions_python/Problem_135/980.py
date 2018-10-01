T = int(raw_input())
for t in range(1, T+1):
    r1 = int(raw_input())
    M1 = [raw_input() for i in range(4)]
    r2 = int(raw_input())
    M2 = [raw_input() for i in range(4)]
    s1 = set(M1[r1 - 1].split())
    s2 = set(M2[r2 - 1].split())
    rs = s1 & s2
    if len(rs) == 0:
        verdict = "Volunteer cheated!"
    elif len(rs) == 1:
        verdict = list(rs)[0]
    else:
        verdict = "Bad magician!"
    print "Case #{t}: {verdict}".format(t=t, verdict=verdict)
