def flipk(row, start, length):
  return row[:start]+flip(row[start:start+length])+row[start+length:]

def flip(pancakes):
  result = ""
  for c in pancakes:
    if c == '+':
      result += '-'
    else:
      result += '+'
  return result

t = int(input())
for i in range(1, t + 1):
  pancakes, flipsize = input().split(" ")
  flipsize = int(flipsize)
  count = 0
  length = len(pancakes)
  for k in range(length-flipsize+1):
    if pancakes[k] == '-':
      pancakes = flipk(pancakes,k,flipsize)
      count += 1
  impossible = False
  for k in range(length-flipsize+1,length):
    if pancakes[k] == '-':
      print("Case #{}: IMPOSSIBLE".format(i))
      impossible = True
      break
  if not impossible:
    print("Case #{}: {}".format(i, count))

