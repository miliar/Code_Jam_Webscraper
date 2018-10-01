import sys

FILENAME = 'B-large.in'
baseElements = []
magic = {}
opposingElements = []


def getCombiningElements(words):
  if len(words) > 0:
    for word in words:
      letters = list(word)
      baseElements.append(letters[0])
      baseElements.append(letters[1])
      one = "".join((letters[0],letters[1]))
      two = "".join((letters[1],letters[0]))
      magic[one] = letters[2]
      magic[two] = letters[2]
      assert getProduct(letters[0], letters[1]) == letters[2]
      assert getProduct(letters[1], letters[0]) == letters[2]
      
def getProduct(elementOne, elementTwo):
  search = "".join([elementOne, elementTwo])
  if search in magic:
    return magic[search]
  return None
  
def getOpposedElements(words):
  if len(words) > 0:
    for word in words:
      letters = list(word)
      opposingElements.append((letters[0], letters[1]))
      opposingElements.append((letters[1], letters[0]))
      assert areOpposed(letters[0], letters[1])
      assert areOpposed(letters[1], letters[0])
  
def areOpposed(elementOne, elementTwo):
  return (elementOne, elementTwo) in opposingElements

textReader = open('%s'  % (FILENAME,), 'r')
numTests = int(textReader.readline())

for T in range(1, numTests + 1):
  baseElements = []
  magic = {}
  opposingElements = []
  line = textReader.readline().split(" ")
  C = int(line[0].strip())
  getCombiningElements(line[1:1+C])  
  D = int(line[C+1].strip())
  getOpposedElements(line[C+2:C+2+D])
  N = int(line[C+2+D].strip())
  invokeElements = list(line[C+3+D].strip())
  
  elements = []
  for element in invokeElements:    
    elements.append(element)
    if len(elements) >= 2:
      product = getProduct(elements[-2], elements[-1])
      if product is not None:
        elements[-2:] = product
      for e in elements:
        if areOpposed(e, elements[-1]):
          elements = []
          break
      
  
  print "Case #" + str(T) + ": [" + ", ".join(elements) +"]"
  
