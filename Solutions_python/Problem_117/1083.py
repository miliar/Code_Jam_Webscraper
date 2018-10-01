
def Solve(res):

    for n in range(len(res)):
        for m in range(len(res[n])):
            height = res[n][m]

            cannot = False
            for row in res[n]:
                if row > height:
                    cannot = True
                    break
            
            if cannot:
                cannot = False
            
                for colid in range(len(res)):
                    if res[colid][m] > height:
                        cannot = True
                        break

            if cannot:
                return "NO"

    return "YES"



f = open('b.in')
T = int(f.readline())
for t in range(T):
    N, M = map(int, f.readline().split())
    lawn = []
    for n in range(N):
        lawn.append(map(int, f.readline().split()))

    #print freq
    result = Solve(lawn)
    print "Case #%d: %s" % (t+1, result)
