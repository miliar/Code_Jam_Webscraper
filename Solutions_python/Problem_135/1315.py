fn = "2014/A-small-attempt0.in"
fo = "2014/A-small-attempt0.out"

class FileHelper():
    def __init__(self, fin,fout):
        self.input   = fin
        self.output  = fout
        self.reader  = open(self.input,"r")
        self.writer  = open(self.output,"w")
        self.cases   = int(self.reader.readline().rstrip())
        self.case_no = 1

    def lineGenerator(self):
        for line in self.reader.readlines():
            yield line.rstrip()
    def printOutput(self, result):
        self.writer.write("Case #%s: %s\n"%(self.case_no,result))
        self.case_no += 1
    def __del__(self):
        self.writer.close()
        self.reader.close()




fh = FileHelper(fn,fo)

for case in range(fh.cases):
    ans1 = int(fh.reader.readline().rstrip())
    before = []
    line1 = fh.reader.readline().split()
    line2 = fh.reader.readline().split()
    line3 = fh.reader.readline().split()
    line4 = fh.reader.readline().split()
    before.append(line1)
    before.append(line2)
    before.append(line3)
    before.append(line4)

    ans2 = int(fh.reader.readline().rstrip())
    after = []
    line5 = fh.reader.readline().split()
    line6 = fh.reader.readline().split()
    line7 = fh.reader.readline().split()
    line8 = fh.reader.readline().split()
    after.append(line5)
    after.append(line6)
    after.append(line7)
    after.append(line8)

    chosen1 = before[ans1-1]
    chosen2 = after[ans2-1]
    total = chosen1 + chosen2
    result = len(total) - len(set(total))
    if result == 1:
        s = set([x for x in total if total.count(x) > 1])
        fh.printOutput("%s"%(s.pop()))
    elif result > 1:
        fh.printOutput("Bad magician!")
    elif result == 0:
        fh.printOutput("Volunteer cheated!")



