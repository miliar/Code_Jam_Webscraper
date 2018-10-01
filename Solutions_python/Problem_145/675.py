from fractions import gcd
import math

f = open('/Users/anna/Mine/Code_Jam_2014/1C/a_sol_small', 'w')  
tasks=[]
N=0
def read_tasks():
    with open('/Users/anna/Mine/Code_Jam_2014/1C/a-small.in.in','r') as f:
    #with open('/Users/anna/Mine/Code_Jam_2014/c_small','r') as f:
        global N
        task=[]
        N=int(f.readline())
        for line in f:    
            tasks.append(map(int, line.split('/')))
  
def solve(P,Q):
   A=gcd(P,Q)
   Q_div=Q/A
   Q_2=math.log(Q_div,2)
   if (Q_2%1==0)and Q_2<40:
       return str(+int(Q_2)-int(math.log(P/A,2)))
   else:
       return "impossible"    

  
read_tasks()
#print tasks[1]
for i in range(N):
   f.write("Case #" + str(i+1)+": "+solve(tasks[i][0],tasks[i][1])+"\n")
   #print "Case #",i+1,": "+solve(tasks[i][0],tasks[i][1])