def binary(n):
    listy = list(bin(n)[2:])
    intlisty = []
    for item in listy:
        intlisty.append(int(item))
    return intlisty
    
outfile = open("outputLarge.txt", "w")

linenum = 0
case = 1
for line in open("C-large.in", "rU"):
    if linenum > 0 and linenum%2 == 0:
        listy = line.split(" ")
        intlisty = []
        for item in listy:
            intlisty.append(int(item))
        maxbinlength = len(bin(max(intlisty))[2:])
        binarylist = [0]*maxbinlength
        targetlist = [0]*maxbinlength
        for number in intlisty:
            numberlist = binary(number)
            numberlist = [0]*(maxbinlength - len(numberlist)) + numberlist
            for index in xrange(0, len(numberlist)):
                binarylist[index] = (binarylist[index] + numberlist[index]) % 2
        if binarylist == targetlist:
            answer = sum(intlisty) - min(intlisty)
            outfile.write("Case #" + str(case) + ": " + str(answer) + "\n") 
        else:
            outfile.write("Case #" + str(case) + ": NO" + "\n")
        case += 1
    linenum += 1

outfile.close()
