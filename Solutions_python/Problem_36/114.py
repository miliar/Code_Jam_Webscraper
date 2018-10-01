def getAllIndex(string, char):
    out=[]
    charCount=string.count(char)
    startIndex=0
    for i in range(charCount):
        startIndex=string.index(char, startIndex)
        out.append(startIndex)
        startIndex+=1
    return out

string="welcome to code jam"

totalcase=int(raw_input())

for casenum in range(totalcase):
    dp=[0 for i in range(len(string))]
    inputline=raw_input()
    for w in inputline:
        allindex=getAllIndex(string, w)
        for index in allindex:
            if index==0:
                dp[0]+=1
            else:
                dp[index]+=dp[index-1]

    print "Case #%d: %04d" % (casenum+1, dp[-1]%10000)
