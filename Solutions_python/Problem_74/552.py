import sys, string

class Parser:
  def __init__(self, inFile):
    self.inFile = inFile
    self.caseRead = 0
    self.numCase = int(self.inFile.readline())    
  def hasNextCase(self):  
    return (self.caseRead < self.numCase)
  def readNextCase(self):
    self.caseRead = self.caseRead + 1
    case = self.inFile.readline().split()
    return case
    
class Processor:
  def __init__(self):
    self.output = ''
  def processCase(self, input):
    numbutton = int(input[0])
    current = { 'B':1, 'O':1 }
    second = { 'B':0, 'O':0 }
    total = 0
    for i in range(numbutton):
      robot = input[2 * i + 1].upper()
      button = int(input[2 * i + 2])
      neededSecond = abs(button - current[robot])
      total = max([second[robot] + neededSecond, total]) + 1
      second[robot] = total
      current[robot] = button
      
    output = [str(total)]
    return output
    
class Printer:
  def __init__(self, outFile):
    self.outFile = outFile
    self.caseNum = 1
  def printCaseOutput(self, output):
    outputStr = ' '.join(output)
    self.outFile.write('Case #' + str(self.caseNum) + ': ' + outputStr + '\n')
    self.caseNum = self.caseNum + 1
        
# run the program
def run(inFileName):
  inFile = open(inFileName, 'r')
  #outFile = sys.stdout
  outFile = open(inFileName + '.out', 'w')
  
  parser = Parser(inFile)
  processor = Processor()
  printer = Printer(outFile)
  while (parser.hasNextCase()):
    printer.printCaseOutput(processor.processCase(parser.readNextCase()))
  
  inFile.close()
  outFile.close()
  
# the main function
def main():
  args = sys.argv[1:]
  if len(args) < 1:
    printf("ERROR: Not enough arguments")
    sys.exit(-1)
  # run: 1st argument --> input file name 
  run(args[0])

# call the main function
if __name__ == '__main__':
  main()
