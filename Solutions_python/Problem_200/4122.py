import sys
def magic(number):
  return int(''.join(str(i) for i in number))




# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
nbrlines = int(input())
for k in range(nbrlines):
  t = input()
  data = [int(i) for i in t]
  i = 1
  addnines = False
  while i < len(data):
    if data[i-1] > data[i]:
      data[i-1] -= 1
      for j in range(i, len(data)):
        data[j] = 9
      addnines = True
      break
    i+=1
  while i > 0 and addnines:
    if data[i-1] > data[i]:
      data[i-1] -= 1
      data[i] = 9
    i -= 1
  print("Case #%i: %i" %(k+1,magic(data)))
