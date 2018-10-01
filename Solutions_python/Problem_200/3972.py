import sys
def calcTidy(number):
  stringNum = str(number)
  result = stringNum[:]
  i = 0
  index = 0
  while(i < len(stringNum)):
    index = len(stringNum) - 1 - i
    if(index - 1 >= 0):
      # do stuff
      if(int(stringNum[index]) < int(stringNum[index-1])):
        stringNum = stringNum[:index-1]+ str(int(stringNum[index-1])-1) + stringNum[index:]
        for j in range(index, len(stringNum)):
          stringNum = stringNum[:j] + "9" + stringNum[j+1:]
    else:
      break
  
    i += 1
  return stringNum

def stripZeroes(inputString):
  for i in range(len(inputString)-1):
    if(inputString[i] == "0"):
      inputString = inputString[:i] + inputString[i+1:]

  return inputString

def main():
  filepath = sys.argv[1]
  with open(filepath) as f:
    content = f.readlines()

  content = [x.strip() for x in content]
  for j in range(len(content)):
    endOfLine = calcTidy(content[j])
    endOfLine = stripZeroes(endOfLine)
    content[j] = "Case #" + str(j) + ": " + str(endOfLine) + "\n"

  target = open("output_numbers.txt", 'w')
  for i in range(len(content)):
    line = content[i]
    if(i == 0):
     continue 
    target.write(content[i])

main()
