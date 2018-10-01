import time
time.clock()

def snap(x,y):
  xx = 2**x
  if(y%xx==xx-1):
      return "ON"
  return "OFF"
  
input = open("A-large.in","r")
output = open("a.out", "w")
t = int(input.readline().strip())
for i in range(t):
  (n,k) = input.readline().split(" ")
  output.write ("Case #"+str(i+1)+": "+snap(int(n),int(k))+"\n")
print(time.clock())
