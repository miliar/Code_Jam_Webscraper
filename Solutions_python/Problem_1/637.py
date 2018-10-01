import sys
class ASolve():
    ncases=0
    nse=0
    nq=0
    SE=[]
    Qu=[]
    curp=0
    curse=0
    St=[]
    cnt=0
    def __init__(self):
        self.SE=[]
        self.Qu=[]
        self.St=[]
        self.nse=int(a.readline().rstrip())
        for i in range(self.nse):
            self.SE.append(a.readline().rstrip())
        self.nq=int(a.readline().rstrip())
        for i in range(self.nq):
            self.Qu.append(a.readline().rstrip())
        print self.SE
        for i in range(self.nse):
            if len(self.Qu)>0 and self.Qu[0]!=self.SE[i]:
                self.St.append([0,i,0,0])
            
    def Switch(self):
        self.cnt=self.cnt+1
        for i in range(self.nse):
            if i!=self.curse:
                self.Inzert(self.curp,i,self.cnt,0)
       
#        self.curse=self.curse+1
#        if self.curse>self.nse-1:
#            self.curse=0
        self.Pick()
        
    def Walk(self):
        while self.curp<=self.nq-1:
            if self.Qu[self.curp]==self.SE[self.curse]:
                self.Switch()
                return
            self.curp=self.curp+1
        self.Inzert(self.curp,self.curse,self.cnt,0)
        self.Pick()
        
    def Inzert(self,cp,cs,cn,vs):
        for i in self.St:
            if i[0]==cp and i[1]==cs :
                return
        self.St.append([cp,cs,cn,vs])
    
    def Pick(self):
        for i in range(len(self.St)):
            if self.St[i][0]<self.nq and self.St[i][3]==0:
#                print self.St[i][0]
                self.curp=self.St[i][0]
                self.curse=self.St[i][1]
                self.cnt=self.St[i][2]
                self.St[i][3]=1
                self.Walk()
                break
    
    def GetSmallest(self):
        x=self.nq
        for i in range(len(self.St)):
           if x>self.St[i][2] and self.St[i][3]==0:
               x=self.St[i][2]
        return x
                
a=file("A-small.in")
b=file("A-small_2.out","w+")
N=int(a.readline().rstrip())
sys.setrecursionlimit(1000000)
for i in range(N):
    x=ASolve()
    x.Pick()
#    print x.St
    print x.GetSmallest()
    b.write("Case #"+str(i+1)+": "+str(x.GetSmallest())+"\n")
    del x
b.close()
a.close()