import re
f = file('A-large.in')
line = f.readline()
L = 0
D = 0
N = 0
result=0
data=[]
dictionary =[]
i = 0
number = 0  
while line[i] <= '9' and line[i] >= '0' :    
  number = number * 10 + int (line[i])
  i = i + 1
L = number
number = 0
i = i + 1
while line[i] <= '9' and line[i] >= '0' :
  number = number * 10 + int (line[i])
  i = i + 1
D = number
number = 0
i = i + 1
while line[i] <= '9' and line[i] >= '0' :
  number = number * 10 + int (line[i])
  i = i + 1
N = number
number = 0
i = 0
tmpd = D
tmpn = N
while tmpd  != 0:
  line = f.readline()
  data.append(line)
  tmpd  -= 1
while tmpn != 0:
  line = f.readline()
  dictionary.append(line)
  tmpn -= 1
f.close()
i = 0
while i < N:
  dictionary[i] = dictionary[i].replace('(','[')
  dictionary[i] = dictionary[i].replace(')',']')

  i+=1
i = 0
number = 0
f = file('A-large.out','w')
while i < N:
  result = 0
  number = 0
  while number < D:
    if re.match(dictionary[i],data[number]):
      result +=1
    number+=1
  i+=1
  f.write("Case #%d: %d\n"  % (i , result))
f.close