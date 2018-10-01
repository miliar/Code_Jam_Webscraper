fin=open("A.in")
fout=open("A.out", "w")
T = int(fin.readline())

for C in range(1, T+1):
    D, N = map(int, fin.readline().split())
    slowest = 0
    for h in range(N):
        P, S = map(int, fin.readline().split())
        slowest = max(slowest, (D-P)/S)
    speed = D/slowest
    fout.write("Case #"+str(C)+": "+str(speed)+"\n")
