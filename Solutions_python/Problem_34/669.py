class AlienLanguage:
    def __init__(self, filename):
        self.F= filename
        self.L=10
        self.D=25
        self.N=10
        self.words=[]
        self.tests=[]

    def loadData(self):
        f=open(self.F,'r')
        datos=f.readline()
        cdat= datos.split(" ")
        self.L=int(cdat[0])
        self.D=int(cdat[1])
        self.N=int(cdat[2])
        p=0
        while(p<self.D):
            self.words.append(f.readline().split("\n")[0])
            p+=1
        p=0
        while(p< self.N):
            self.tests.append(f.readline().split("\n")[0])
            p+=1
        
        
    def evaluateWord(self, word, test):
        currentI=0
        cumple=True
        for l in word:
            posL=self.getPosList(currentI, test)
            currentI=posL[-1]
            if not posL.__contains__(l):
                cumple=False
                break
                
        
        return cumple

    def getPosList(self,i, test):
        res=[]
        if test[i]=="(":
            i+=1
            while not test[i]==")":
                res.append(test[i])
                i+=1
            res.append(i+1)
            return res
            
        else:
            return [test[i], i+1]

    def makeOutput(self ):
        self.loadData()
        testCount=[0 for i in range(0,self.N )]
        print testCount
        for i,t in enumerate(self.tests):
            for w in self.words:
                if self.evaluateWord(w,t):
                    testCount[i]+=1
        f=open("A-large.out", "w")
        for i,c in enumerate(testCount):
            f.write("Case #"+str(i+1)+": " + str(c)+ "\n")
        
        print testCount


al=AlienLanguage('A-large.in')
al.makeOutput()
