import re

f = open("A-large.in", "r")

line = f.readline()
ldn = line.split()
l = (int) (ldn[0])
d = (int) (ldn[1])
n = (int) (ldn[2])
##print ("l = ", l)
##print ("d = ", d)
##print ("n = ", n)

words = []
for i in range(d):
    words.append(f.readline().strip())
##print (words)

wordlist = "\n".join(words)

cases = []
for i in range(n):
    case = f.readline().strip()
    case = case.replace("(", "[")
    case = case.replace(")", "]")
    cases.append(case)
##print (cases)

for i, case in enumerate(cases):
    m = re.findall(case, wordlist)
    print ("Case #{0}: {1}".format(i + 1, len(m))) 

f.close()
