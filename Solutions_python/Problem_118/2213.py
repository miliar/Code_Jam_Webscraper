import math

inputfile = "C-small-attempt0.in"
outputfile = inputfile + ".output"
input = open(inputfile).read()
output = open(outputfile, "w")

def isPalindrome(num):
  num = str(num)
  length = len(num)
  for i in range(length / 2):
    if (num[i] != num[-(1 + i)]):
      return False
  return True

def isFairSquare(num):
  sqrt = math.sqrt(num)
  if (round(sqrt) != sqrt):
    return False
  sqrt = int(sqrt)
  return isPalindrome(num) and isPalindrome(sqrt)

def evaluate(start, end):
  count = 0
  for i in range(start, end + 1):
    if (isFairSquare(i)):
      count += 1
  return str(count)

cases = int(input.split("\n")[0])
input = input.split("\n")[1:]
for i in range(cases):
  start, end = map(lambda x: int(x), input[i].split())
  outputline = "Case #" + str(i + 1) + ": " + evaluate(start, end) + "\n"
  output.write(outputline)
output.close()
