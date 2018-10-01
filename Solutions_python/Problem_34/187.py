#Location = "A-small-attempt1.in"
Location = "A-large.in"

file = open(Location)
line = file.readline()
(L, D, N) = line.split(" ")[0:3]
words = []
for i in range(0, int(D)):
  words.append(file.readline()[0:int(L)])

output = open("output", "w")
for i in range(0, int(N)):
#for i in range(0, 2):
  switch = 0
  first = 0
  answer = 0
  case = file.readline().strip("\n")
  letters = []
  for j in case:
    if j == '(':
      switch = True
    elif j == ')':
      switch = False
      first = False
    else:
      if switch == False:
        letters.append(j)
      else:
        if first == False:
          letters.append(j)
          first = True
        else:
          letters[len(letters) - 1] = letters[len(letters) - 1] + j
  if len(letters) == int(L):
    newwords = []
    for word in words:
      newwords.append(word)
    for j in range(0, int(L)):
      trywords = []
      letter = letters[j]
      for poss in letter:
        for word in newwords:
          if poss == word[j]:
            trywords.append(word)
      newwords = trywords
    answer = len(newwords)
  else:
    print "Case " + str(i + 1) + " possibly failed"
  output.write("Case #" + str(i + 1) + ": " + str(answer) + "\n")
file.close()
output.close()
