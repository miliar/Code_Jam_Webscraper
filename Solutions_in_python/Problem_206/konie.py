



def finaltime(way, d):
    n = len(way)
    t = 0 # final time
    
    for i in range(n)[::-1]:
        rest = d - way[i][0] # tyle zostalo
        sofar = way[i][1] * t
        rest -= sofar
        if rest > 0:
            t += rest / float(way[i][1])
        #gdzie po tym czasi bedzie poprzedni kon?
        #pzesuwam konia o tyle ile szli poprzednicy i dodaje do to czas tego konia

    return t

if __name__ == "__main__":
    
    f = open("inputl.txt")
    lines = f.readlines()
    f.close()
    t = int(lines[0])
    i = 1
    lc = 1
    
    while i <= t:
#        print "t, i %d %d" % (t, i)
        way = []
        d, n = map(int, lines[lc].strip().split(' '))
        for j in range(n):
            lc+=1
            k, s = map(int, lines[lc].strip().split(' '))
            way.append([k, s])
        time = finaltime(sorted(way), d)
        print "Case #%d: %.6f" % (i, d/time)
        i += 1
        lc += 1


