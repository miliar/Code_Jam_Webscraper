
f_in = open("input.txt",'r')
f_out = open("output.txt","w")
inp = f_in.readlines()

N = eval(inp[0])


for z in range (N):
 guests=0;
 k = eval(inp[z+1][0:1]) #Shymax
 line = list(inp[z+1][2:len(inp[z+1])-1]) #List of people
 total=0
 
 for i in range (k+1): #loop through levels of shyness
  total+=eval(line[i]) #track number standing
  if(eval(line[i])==0): #if a gap, check wether would affect next level
   if(i>total):
    guests+=1
 f_out.write("Case #"+str((z+1))+": "+str(guests))

f_out.close()
