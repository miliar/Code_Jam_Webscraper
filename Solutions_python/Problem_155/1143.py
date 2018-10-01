inFile = open("C:\\Users\\Eric\\Downloads\\infile.in", "r")
outFile = open("C:\\Users\\Eric\\Downloads\\outfile.out", "w")
inString = inFile.readline()
numOfTestCase = int(inString)

for i in range(numOfTestCase):
    inputString = inFile.readline()[:-1]
    if inputString.find(" ") > 0:
        Smax, s = inputString.split(" ")
    else:
        Smax = inputString
        s = "0"
    s = list(s)
    need = 0
    stand = 0
    remain = 0
    for j in range(len(s)):
        if stand >= j:
            stand += int(s[j])
            s[j] = '0'
        else:
            remain += int(s[j])
    while remain != 0:
        need += 1
        stand += 1
        for j in range(len(s)):
            if stand >= j:
                stand += int(s[j])
                remain -= int(s[j])
                s[j] = '0'
    outFile.write("Case #"+str(i+1)+": "+str(need) + '\n')
            
outFile.close()
inFile.close()
