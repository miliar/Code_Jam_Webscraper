'''
Created on Apr 12, 2013

@author: Moatasem
'''
import math

def getSolution(r,t):
   sol1=(-1*(2*r-1)+math.sqrt((2*r-1)**2+8*t))/4
  # sol2=(-1*(2*r-1)-math.sqrt(math.pow(2*r-1, 2)+8*t))/4
   return sol1




f_r = open('A.in',"r")
n_test=int(f_r.readline().strip()) 
print n_test
result=""
f_w = open("A.out", "w")
for i in range(n_test):
    temp=map(float,f_r.readline().split())
    sol= getSolution(temp[0],temp[1])
    print int(sol)
    output_str='Case #{itr}: {res}'.format(itr=(i+1),res=int(sol))
    f_w.write(output_str+'\n')
f_r.close()
f_w.close()
