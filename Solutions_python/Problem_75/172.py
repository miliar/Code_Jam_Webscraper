'''
@author: Peratham
'''

INPUTFILE = 'B-large.in'
OUTPUTFILE = 'B-large.out'

class potToll:
    def __init__(self, tc, to):
        self.tc = tc
        self.to = to
        self.toll = []
        
    def add(self, inchar):
        self.toll.append(inchar)
        self.checkCombine()
        self.checkOppose()
        
    
    def meetCombineCond(self, l1, l2, tm1, tm2):
        if l1 == tm1 and l2 == tm2:
            return True
        if l1 == tm2 and l2 == tm1:
            return True
        return False
        
    def checkCombine(self):
        if len(self.toll) < 2 or len(self.tc) < 1:
            return
        l1 = self.toll[-1]
        l2 = self.toll[-2]
        for rule in self.tc:
            tm1 = rule[0]
            tm2 = rule[1]
            if self.meetCombineCond(l1, l2, tm1, tm2):
                self.toll.pop()
                self.toll.pop()
                self.toll.append(rule[-1])
                break
                
    def checkOppose(self):
        if len(self.toll) < 2 or len(self.to) < 1:
            return
        for rule in self.to:
            if self.toll.count(rule[0]) > 0 and self.toll.count(rule[1]) > 0:
                self.toll = []
                break
                
    
def readFile():
    file = open(INPUTFILE, 'r')
    text = file.readline()
    tmp = text.split()
    P = tmp[0]
    
    param = []
    param.append(P)
    input = []
    combine = []
    oppose = []
    
    text = file.readlines()
    for line in text:
        tc = []
        to = []
        tmp = line.split()
        num_com = int(tmp[0])
        for itmp in tmp[1:1 + num_com]:
            tc.append(itmp)
        num_opp = int(tmp[num_com + 1])
        for itmp in tmp[num_com + 2:num_com + 2 + num_opp]:
            to.append(itmp)
        input.append(tmp[-1])
        combine.append(tc)
        oppose.append(to)
        
    param.append(combine)
    param.append(oppose)
    
    file.close()
    del file
    return [param, input]
    
def solve(param, input):
    ans = []
    tc = param[1]
    to = param[2]
    cnt = 0
    for iput in input:
        pot = potToll(tc[cnt], to[cnt])
        cnt += 1
        for ichar in iput:
            pot.add(ichar)
        ans.append(pot.toll)
    return ans

def writeFile(ans):
    file = open(OUTPUTFILE, 'w')
    file.write("Case #1: [")
    no = True
    for i in ans[0]:
        if no:
            file.write(i)
            no = False
        else:
            file.write(", " + i)
    file.write("]\n")
    file.close()
    
    file = open(OUTPUTFILE, 'a')
    for i in xrange(len(ans) - 1):
        file.write("Case #%d: [" % (i + 2))
        no = True
        for i in ans[i + 1]:
            if no:
                file.write(i)
                no = False
            else:
                file.write(", " + i)
        file.write("]\n")
        
    file.close()

def main():
    [param, input] = readFile()
    ans = solve(param, input)
    writeFile(ans)

if __name__ == '__main__':
    main()
