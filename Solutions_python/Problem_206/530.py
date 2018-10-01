

def steed2(finish, d):
    l = []
    for horse in d:
        l.append( (finish - horse) / float(d[horse]) )
    l = sorted(l, reverse = True)
    return finish / l[0]



if __name__ == '__main__':
    inputName = "largeSteed.txt"
    outputName = "outputLargeSteed.txt"
    f = open("/Users/benhubsch/Dropbox/Side Projects/Google Code Jam/Round 2A/" + inputName,'r')
    w = open("/Users/benhubsch/Dropbox/Side Projects/Google Code Jam/Round 2A/" + outputName,'w')
    cases = int(f.readline())
    c = 1
    while cases > 0:
        first = f.readline().split()
        finish, numHorses = int(first[0]), int(first[1])
        d = {}
        for num in range(numHorses):
            currHorse = f.readline().split()
            d[int(currHorse[0])] = int(currHorse[1])
        w.write("Case #" + str(c) + ": " + str(steed2(finish, d)) + "\n")
        cases -= 1
        c += 1
    f.close()
    w.close()
    print(steed2(300, {60:90, 120:60}))
