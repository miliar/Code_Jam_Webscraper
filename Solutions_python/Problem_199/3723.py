f = open("A-large.in","r")
g = open("output_pancake.txt","w")

info = f.read().split("\n")
n = int(info.pop(0))
print n
print info

def findMinus(string):
   for j in range(len(string)):
      if string[j]=="-":
         #print "hi"
         return str(j)
   return "-1"

def flip(string,a,b):
   sub = string[a:b+1]
   front = string[:a]
   back = string[b+1:]
   for i in range(len(sub)):
      if sub[i]=="+":
         sub = sub[:i]+ "-" + sub[i+1:]
      else:
         sub = sub[:i]+ "+" + sub[i+1:]
   return front + sub + back
   
for i in range(n):
   table = info[i].split(" ")[0]
   K = int(info[i].split(" ")[1])
   ind = 0
   counter=0
   while findMinus(table) != "-1":
      ind = int(findMinus(table))
      if ind+K>len(table):
         break

      table = flip(table,ind,ind+K-1)
      print table
      counter+=1
   if findMinus(table) == "-1":
      g.write("Case #" + str(i+1) + ": " + str(counter) + "\n")     
   else:
      g.write("Case #" + str(i+1) + ": " + "IMPOSSIBLE" + "\n")
      
   
   
   
   
   
   
   
   
 