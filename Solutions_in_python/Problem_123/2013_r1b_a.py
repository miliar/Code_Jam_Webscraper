import sys


def solve(start, motes, i=0):

    m=start
    if i==len(motes):
        return 0

    #print "%d Armin: %d, next:%d" % (i, m, motes[i])

    #zug klappt, alles prima
    if m>motes[i]:
        m+=motes[i]
        return solve(m, motes, i+1)

    #wenn hinzufuegen nix bringt, dann sofort loeschen
    if m-1==0:
        return 1+solve(m, motes, i+1)

    #zwei varianten ausprobieren

    # eins hinzufuegen
    c1 = 1+solve(m+m-1, motes, i)
    #einfach das aktuelle ignorieren
    c2 = 1+solve(m, motes, i+1)
    #print "hinzufuegen: %d, loeschen: %d" % (c1,c2)
    return min(c1, c2)
            
fp = file(sys.argv[1])

for t in range(int(fp.readline())):
    a, n = map(int, fp.readline().split())
    motes = map(int, fp.readline().split())
    print "Case #%d: %d" % (t+1, solve(a, sorted(motes)))
    
    
