def minvec(veca,vecb):
    veca.sort()
    vecb.sort()
    vecb.reverse()
    ans = 0
    for a in range(len(veca)):
        ans += veca[a]*vecb[a]
    return(str(ans))
try:
    f = open("input/A-large.in")
    fout = open("input/A-large.out",'w')
    for case in range(int(f.readline())):
        f.readline()
        veca = map(int, f.readline().split())
        vecb = map(int, f.readline().split())
        fout.write("Case #" + str(case+1) + ": " + minvec(veca, vecb) + "\n")
    f.close()
    fout.close()
except:
    f.close()
    fout.close()