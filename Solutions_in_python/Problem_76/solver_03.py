import sys # For argv

def getSum(pile) : 
 # Get the 'sum' of a pile, according to Patrick
 t = 0
 for i in pile : 
  t ^= i # Inspection tells us that Patrick's addition is equivalent to XORing
 return t#  the two numbers

def isPossible(candies) : 
 return getSum(candies) == 0 # A-ha! If xor(a) = xor(b) then a xor b == 0!

def solve(line,f,caseno) :
 candies = map(int,line.split(" "))
 if isPossible(candies) :
  f.write("Case #%d: %d\n"%(caseno,sum(candies) - min(candies)))
 else : 
  f.write("Case #%d: NO\n"%caseno)

filename = sys.argv[1]
f = open(filename)
inpt = f.read()
f.close()
inpt_lines = inpt.split("\n")
cases = int(inpt_lines[0])
f = open(sys.argv[2],"w")
caseno = 1
x = 0 # Skipping the lines that specify the count is just alternating lines.
for i in inpt_lines[1:1+2*cases] :
 x += 1
 if x%2 == 1 :
  continue
 solve(i,f,caseno)
 caseno += 1
 
f.close()


