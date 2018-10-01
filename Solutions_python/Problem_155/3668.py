f = open('A-small-attempt5.in','r')
fout = open('outputOpera.txt','w')

f.readline()

case = 0
for line in f:
  case += 1
  data = line.rstrip().split()
  maxShy = int(data[0])
  audData = data[1]
  aud = {}
  counter = 0
  for member in audData:
    member = int(member)
    aud[counter] = member 
    counter += 1
  needed = 0
  people = 0
  for shyLevel in range(maxShy+1):
    if shyLevel > people:
      needed += shyLevel-people
      people += shyLevel-people
    people += aud[shyLevel]

  fout.write("Case #"+str(case)+": "+str(needed)+"\n")
f.close()
fout.close()
