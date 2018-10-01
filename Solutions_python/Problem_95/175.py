import collections
f_in = open("qa2.input", 'r')
f_out = open("output.txt", 'w')

inputs = f_in.read().split('\n')


numTests = int(inputs[0])
print numTests
count = collections.defaultdict(int)
frequencyStat = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']
match = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}


#chars = ''.join(inputs[1:]).replace(' ', '')

#for c in chars:
#  count[c] += 1

# return sorted chars by its count in descending order
#res = list(sorted(count, key=count.__getitem__, reverse=True))
#
#for i in range(len(res)):
#  match[res[i]] = frequencyStat[i]

for lineNum in range(1, numTests+1):
  newLine=[]
  for c in inputs[lineNum]:
    if match.has_key(c):
      newLine.append(match[c])
    else:
      newLine.append(c)
  lineout =  "Case #" + str(lineNum) + ": " + ''.join(newLine)
  print lineout
  f_out.write(lineout + "\n")
  
f_out.close()
f_in.close()