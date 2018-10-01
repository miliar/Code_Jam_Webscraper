#
import re
import math
         
f = open("A-small-attempt0.in","r")
fo = open("A_small.out","w")



lines = f.readlines()
lines = [l.strip() for l in lines]
i = 0
T = int(lines.pop(0))
for icase in range(T):
      # set parameters
      [ans1] = lines.pop(0)
      grid1 = []
      for i in range(4):
          grid1.append({ x for x in re.split(" ",lines.pop(0)) })
      line0 = {x for x in grid1[int(ans1) -1]}
      line1 = {x for x in grid1[int(ans1) -1]}
      [ans2] = lines.pop(0)
      grid2 = []
      for i in range(4):
          grid2.append({ x for x in re.split(" ",lines.pop(0)) })
      line2 = grid2[int(ans2) -1]
      line0.update(line2)
      #print(line1)      
      #print(line2)
      #print(line0)      
      #print(A,B)
      ans = len(line1 & line2)
      if ans == 0:
          ans = "Volunteer cheated!"
          print("Case #",icase+1,": ",ans,sep="",file=fo)
          print("Case #",icase+1,": ",ans,sep="")
      elif ans >= 2:
          ans = "Bad magician!"
          print("Case #",icase+1,": ",ans,sep="",file=fo)
          print("Case #",icase+1,": ",ans,sep="")
      else:
          x = line1 & line2
          ans = x.pop()
          print("Case #",icase+1,": ",ans,sep="",file=fo)
          print("Case #",icase+1,": ",ans,sep="")
          
#print("Case #",icase+1,": ",nswitch,sep="",file=fo)
f.close()
fo.close()

