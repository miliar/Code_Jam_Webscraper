#fileName=str('C:\\Users\\Soheil\\Downloads\\A-small-attempt1.in')
#fileName='C:\\Users\\Soheil\\Documents\\qA.txt'
fileName=str('C:\\Users\\Soheil\\Downloads\\A-large.in')
fin = open(fileName,'r')
fout = open('C:\\Users\\Soheil\\Documents\\outputfilelarge.txt', 'w')

def Flip(s):
    if(s=='+'):
        s='-'
    elif(s=='-'):
        s='+'
    return s

def FlipPanCakes(pancakes,index, flipperSize):
    for i in range(index,index+flipperSize-1):
        pancakes[i]=Flip(pancakes[i])
    return pancakes

t = int(fin.readline())  # read a line with a single integer
print(t)
for i in range(1, t+1):
  #a = [str(s)for s in fin.readline()]
  a=str(fin.readline()).split()
  
  S = list(a[0])
  k = int(a[1])
  numberOfFlips=0;
  index=1;
  possibleSolution=True
  for letter in S:
    if(letter=='-'):
     if(index+k<=len(S)+1):
        S=FlipPanCakes(S,index,k)
        numberOfFlips=numberOfFlips+1
     else:
        possibleSolution=False
    index=index+1
  if(possibleSolution):
    fout.write("Case #{}: {}\n".format(i,numberOfFlips))
  else:
    fout.write("Case #{}: {}\n".format(i,"IMPOSSIBLE"))
  
fout.close()
fin.close()
main.run()

