
class Solution:
    def __init__(self,X,R,C):
        self.dat=[X,R,C]
    def result(self):
        X,R,C=self.dat
        if R*C%X!=0 or max(R,C)<X or X>=7 or (X+1)//2>min(R,C):
            return 'RICHARD'
        elif X in [1,2,3]:
            return 'GABRIEL'
        elif X==4:
            minv=2
            if min(R,C)<=minv: return 'RICHARD'
            else: return 'GABRIEL'
        elif X==5:
            minv=3
            if min(R,C)<minv or (min(R,C)==3 and max(R,C)<10): return 'RICHARD'
            else: return 'GABRIEL'
        elif X==6:
            minv=3
            if min(R,C)<=minv: return 'RICHARD'
            else: return 'GABRIEL'
        
with open('testin.txt','r') as f:
	data=f.readlines()

N=int(data[0])
res=""

start,delta=1,1
for i in range(N):
    X,R,C=map(int,data[start].split())
    x=Solution(X,R,C)
    res+="Case #{}: {}\n".format(i+1,x.result())
    start+=delta
    print 'finished case %d'%i

with open('res.txt', 'w') as f:
	f.write(res)