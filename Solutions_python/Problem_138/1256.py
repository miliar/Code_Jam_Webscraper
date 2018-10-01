fn = "2014/D-large.in"
fo = "2014/D-large.out"

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

def magicTrick(fh):
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

def cookieClicker(fh):
    for line in fh.lineGenerator():
        params = line.split()
        C = float(params[0]) #Cookies to buy farm
        F = float(params[1]) #+Cookies per second per farm
        X = float(params[2]) #goal cookies
        cps = 2.0            #Cookies per second
        timeLapse = 0

        t1 = X/cps
        buyFarm = C/cps
        t2 = buyFarm + X/(cps+F)
        while t2 < t1:
            timeLapse +=buyFarm
            cps += F
            t1 = X/cps
            buyFarm = C/cps
            t2 = buyFarm + X/(cps+F)
        timeLapse += t1

        fh.printOutput("%.7f"%timeLapse)

def mineSweeper(fh):
    for line in fh.lineGenerator():
        output = "\n"
        params = line.split()
        R = int(params[0])
        C = int(params[1])
        M = int(params[2])
        space = R*C - M
    pass

def war(fh):
    for case in range(fh.cases):
        N = int(fh.reader.readline())

        nao = [float(i) for i in fh.reader.readline().rstrip().split()]
        ken = [float(i) for i in fh.reader.readline().rstrip().split()]
        nao = sorted(nao)
        ken = sorted(ken)
        y = 0 # y = cheat mode
        z = 0
        # z = normal mode
        weights = []
        weights.extend(nao)
        weights.extend(ken)
        weights = sorted(weights)

        weights2 = list(weights)
        nao2 = list(nao)
        ken2 = list(ken)

        for i in range(N):
            #cheat mode
            if weights[0] in nao:
                weights.remove(ken.pop())
                weights.remove(nao.pop(0))
            else:
                weights.remove(ken.pop(0))
                weights.remove(nao.pop(0))
                y += 1

            #normal mode
            if weights2[-1] in nao2:
                weights2.remove(nao2.pop())
                weights2.remove(ken2.pop(0))
                z+=1
            else:
                weights2.remove(nao2.pop())
                weights2.remove(ken2.pop())

        fh.printOutput("%s %s"%(y,z))

war(fh)

