welcomeStr = "welcome to code jam"

def subseqCount(s, sc, wc):
    nwChar = welcomeStr[wc]
    sChar = s[sc]
    count = 0
    for i in range(sc, len(s)):
        if s[i] == nwChar:
            if wc+1 < len(welcomeStr):
                count += subseqCount(s, i+1, wc+1)
            else:
                count += 1
    return count

class WelcomeToGoogleCodeJam:
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
        self.inf = open(self.infile, "r")
        self.outf = open(self.outfile, "w")
        self.parseInput()
        self.getSubSeqCount()
        self.inf.close()
        self.outf.close()

    def parseInput(self):
        self.N = int(self.inf.readline())
        self.lines = []
        for i in range(self.N):
            self.lines.append(self.inf.readline())
        #print self.lines

    def getSubSeqCount(self):
        tc = 1
        for line in self.lines:
            #print line
            count = subseqCount(line, 0, 0)
            self.outf.write("Case #" + str(tc) + ": ")
            self.outf.write("%04d" % count)
            self.outf.write("\n")
            tc += 1

if __name__ =="__main__":
    #wt = WelcomeToGoogleCodeJam("in.txt", "out.txt")
    wts = WelcomeToGoogleCodeJam("C-small-attempt1.in", "C-small-attempt1.out")
