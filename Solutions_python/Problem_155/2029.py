








def calcMinFriends(shyArr):
    #print shyArr
    minFriends = 0
    maxShy = len(shyArr)
    standing = shyArr[0]
    for si in range(1,maxShy):
        if shyArr[si] > 0 and si > standing:
            newFriends = (si-standing)
            minFriends += newFriends
            standing += newFriends + shyArr[si]
        else:
            standing += shyArr[si]
    return minFriends
        
        









if __name__ == "__main__":
#    fin = open("A-small-attempt1.in.txt")
#    fout = open("A-small-output.txt","w")
    fin = open("A-large.in.txt")
    fout = open("A-large-output.txt","w")
    nCases = int(fin.readline())
    
    for c in xrange(nCases):
        line = fin.readline()
        (maxShy, shyString) = line.split()
        shyArr = []
        for si in shyString:
            shyArr.append(int(si))
        minFriends = calcMinFriends(shyArr)
        
        fout.write("Case #{0}: {1}\n".format((c+1), minFriends))
        
    fout.close()    
    fin.close()