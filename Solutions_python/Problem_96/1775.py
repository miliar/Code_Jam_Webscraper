#!/usr/bin/python

def Ncases(S,p,arr):
  r=0
  for G in arr:
 
    if ((G-1)/3+1) >= p:
      r+=1
    elif (G>= (p+max(0,p-2)+max(0,p-2))) and (S > 0):
      r+=1
      S-=1
  return r

f=open("B-large.in", "r")
text=f.read()

lines=text.split("\n")
#print lines[0]
i=0
for line in lines[1:len(lines)-1]:
  Numbers = line.split(" ")
  
  N=int(Numbers[0])
  S=int(Numbers[1])
  p=int(Numbers[2])
  arr=[]
  
  #print Numbers[3:(3+N)]
  for k in Numbers[3:(N+3)]:
    #print k
    arr.append(int(k))
  print 'Case #{0}: {1}'.format(i+1, Ncases(S,p,arr))
  #print "Case #",i," :",Ncases(S,p,arr)
  i+=1
  #print N
  #print S
  #print p
  #print arr
#print(Ncases(1,5,[15,13,11]))

#print(Ncases(0, 8, [23, 22, 21]))
#print(Ncases( 1, 1, [8, 0]))
#print(Ncases( 2, 8, [29, 20, 8, 18, 18, 21]))


