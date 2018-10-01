from itertools import islice

class OneA:

    n = 0 #number of cases
    currcase = 0

    created = []
    tobe = []
    filedata = []
    
    inputfile = "onea.in"
    outputfile = "onea.out"
    
    def __init__(self):
        self.solvetheproblem()

    def solvetheproblem(self):
        f = open(self.inputfile)
        g = open(self.outputfile,'a')
        
        with open(self.inputfile) as myfile:
            cases=list(islice(myfile,1))
            self.n = int(cases[0])

        for lines in f:
            self.filedata.append(lines[0:len(lines)-1])
        #Use this when cases span multiple lines:
        #for i in range(1,2*self.n,2):
        index = 1
        case = 1
        for i in range(1,self.n+1):

            with open(self.inputfile) as myfile:
                self.created.append("/")
                info=list(islice(myfile,index,index+1))
                lines = info[0][0:len(info[0])-1].split(" ")
                N = int(lines[0])
                M = int(lines[1])
                for j in range(index+1,index + N + 1):
                    self.created.append(self.filedata[j])
                for j in range(index+N+1,index + N + M + 1):
                    self.tobe.append(self.filedata[j])

                self.currcase = case
                a = self.solvesingle()
                case = case+1
                g.write("Case #" + str(self.currcase) + ": " + str(a) + "\n")
                print a
                print "..."
                print case
                # print self.created
                # print self.tobe
                # print N
                # print M

                self.created = []
                self.tobe = []
                index = index + N + M + 1
            
    def solvesingle(self):
        ans = 0
        new = []

        for x in self.tobe:
            if x in self.created:
                continue

            y = x.split("/")
            for lens in range(0,len(y)+1):
                z = "/".join(y[0:len(y)-lens])
                if(z == ""):
                    z = "/"
                new.append(z)

                if z in self.created:
                    for stuff in new:
                        self.created.append(stuff)
                    break
                ans = ans+1
                #print self.created

        return ans
                    
