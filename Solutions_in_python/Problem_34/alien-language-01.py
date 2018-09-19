
def sanitize(wlist):
  newlist = []
  for i in wlist:
      if i[0]!='(':
        for letter in i:
          newlist = newlist + [str(letter)]
      else:  
        newlist = newlist + [i];
  return newlist

f = open('A-large.in', 'r')
outfile = open('A-large.out', 'w')

line = f.readline()

L, D, N = (line.split())

L = int(L)
D = int(D)
N = int(N)

dic = []

for i in range(1, D+1):
  line = f.readline()
  dic = dic + [line.strip()]
  
strs = []
loop_counter = 1
while 1:
  count = 0
  line = f.readline()
  if not line:
    break
  if len(line.strip())==0:
    break
    
  line=line.replace("(", " (")
  line=line.replace(")", ") ")
  tokens = line.split()
  tokens  = sanitize(tokens)

  for word in dic:
    letter_count = 0
    flag = 1
    
    for letter in word:
      if letter not in tokens[letter_count]:
        flag = 0
        break
      letter_count = letter_count + 1
    if flag == 1:
      count = count +1
  outfile.write( "Case #" +str(loop_counter) + ": "+str(count)+"\n")
  loop_counter = loop_counter+1
f.close()
outfile.close()


