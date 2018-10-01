import sys
import re
filename = "C:\\Amir\\programming\\CodeJam\\first\\1\\in.txt"
f = open(filename)
lines = f.readlines()
f.close()
lines.reverse()
firstLine = lines.pop().split(" ")
#print firstLine
L = int(firstLine[0])
D = int(firstLine[1])
N = int(firstLine[2])
#print "N=",str(N)
dic = {}
for i in range(D):
    dic[lines.pop()] = True
out = open("C:\\Amir\\programming\\CodeJam\\first\\1\\out.txt",'w')
for j in range(N):
    line = lines.pop()
    line = line.replace("(","[").replace(")","]")
  #  print line
    cnt = 0
    for word in dic.keys():
        if (re.match(line,word)):
            cnt += 1
 #   print cnt
    out.write("Case #"+str(j+1)+": "+str(cnt)+"\n")
out.close()
