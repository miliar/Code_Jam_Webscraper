
class TestCase:

    def __init__(self, n, d):
        self.n = n
        self.max = d
        self.result = conv(d)
        #self.calc()

    def p(self):
        return 'Case #{}: {}\n'.format(self.n,self.result)

    def calc(self):
        n = self.max
        while True:
            if isTidy(n):
                self.result = n
                return
            n=n-1



def map(strarry):
    v = strarry.split(' ')
    r = []
    for u in v:
        r.append(int(u))
    return r

def isTidy(n):
    s = str(n)
    if len(s) == 1:
        return True
    l = s[0]
    for i in range(1, len(s)):
        if s[i] < l:
            return False
        l = s[i]
    return True;

def conv(n):
    s=list(str(n))
    if len(s) == 1:
        return n
    for i in range(len(s)-1,0,-1):
        # print i
        # print s[i]
        # print s
        if s[i] < s[i-1]:
            for j in range(i,len(s)):
                s[j]='9'
            s[i - 1] = str(int(s[i - 1]) - 1)
            # if i==1 and s[i-1] == 1:
            #     s[i-1]=' '
            # else:
            #     s[i-1]=str(int(s[i-1])-1)
    #print s
    return int("".join(s))

# print '{} -> {}'.format(882,conv(882))
# print '{} -> {}'.format(110,conv(110))

inFile = 'B-large.in'
outFile = inFile.replace('.in', '.out')

inf = open(inFile, 'r')
outf = open(outFile, 'w')

data = inf.readlines()
noTests = int(data[0])
i=1
for d in data[1:]:
    tc = TestCase(i, int(d))
    outf.write(tc.p())
    print tc.p()
    i=i+1

outf.close()
inf.close()

