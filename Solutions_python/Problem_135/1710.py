import sys
import math


path = "/Users/yongc0916/Downloads/"
testFile = open(path + "C-large-practice-1.in", 'r')
fil = open(path+"output.txt", 'w+')
rlist = testFile.readlines()
numTest = rlist[0]
rlist = rlist[1:]

def checkResult(l1, l2):
   dups = (set(l1) & set(l2))
   if (len(dups) > 1):
      return "Bad magician!"
   elif (len(dups) < 1):
      return "Volunteer cheated!"
   else:
      return str(list(dups)[0])


for num in range(int(numTest)):
   row1 = rlist[0]
   row2 = rlist[5]
   list1 = rlist[int(row1[0])]
   list2 = rlist[int(row2[0]) + 5]
   ans = checkResult(list1.split(), list2.split())
   fil.write("Case #" + str(num+1) + ": " + ans + "\n")
   if (len(rlist) > 10):
      rlist = rlist[10:]

fil.close()