import sys

if len(sys.argv) < 2:
  raise RuntimeError("Please give the name of the input file") 

inputfilename = str(sys.argv[1])
outputfilename = inputfilename.replace('in','out')
  
f_in = open(inputfilename, 'r')
f_out = open(outputfilename, 'w')


# A Node in a tree
class Node:
  def __init__ (self, val):
    self.name = val
    self.children = list()
  
  def val_in_children(self, val):
    for child in self.children:
      if child.name.strip() == val.strip():
        return child

    return None

  def print_tree(self):
    for child in self.children:
      print child.name
    
    for child in self.children:
      child.print_tree()


# print the values passed
def output(num_test, value, fileref = f_out):
  fileref.write("Case #"+ str(num_test)+": "+str(value)+"\n")

# Return an n-dimensional array of zeros. Dimensions passed
# as arguments
def zeros(*shape):
  if len(shape) == 0:
    return 0
  car = shape[0]
  cdr = shape[1:]
  return [zeros(*cdr) for i in range(car)]

# Read a line (or multiple lines) from the input.
# If it is a single line then convert into list of ints
# If multiple lines then convert into lists of lists (i.e. 
# two-dimensional array
# If no arguments then reads a single line from f_in
def read_and_convert(linenum = 1, fileref = f_in):

  intlist = list()

  for line in range(0, linenum):  
    strlist = fileref.readline().split()
 
    tmplist = list()  
  
    for string in strlist:
      tmplist.append(int(string))

    if linenum == 1:
      intlist.extend(tmplist)
    else:
      intlist.append(tmplist)
  return intlist

# Write your code here
def runtest(numtest):
  line = read_and_convert()
  sums = line[3:]

  num_googlers= line[0]
  num_surp = line[1]
  req_val = line[2]

  print num_googlers, " ", num_surp, " ", req_val

  even_googlers = 0
  even_surp = 0      #no of googlers whose only consecutive combo is surprising
  odd_googlers = 0
  odd_surp = 0       #no of googlers whose only distance 2 combo is surprising

  for x in sums:
    div = int(x/3)

    if x % 3 == 0:
      if x == 0 and req_val == 0:
        even_googlers = even_googlers + 1
      elif x > 0 and div >= req_val:
        even_googlers = even_googlers + 1      
      elif x > 0 and div+1 >= req_val:
        even_surp = even_surp + 1 
    else:
      next = div + 1
      next2 = div + 2
    
      if x - (div * 3) == 1:
        if next >= req_val:
          odd_googlers = odd_googlers + 1
      elif x - (div * 3) == 2:
        if next >= req_val:
          odd_googlers = odd_googlers + 1
        elif next2 >= req_val:
          odd_surp = odd_surp + 1     
  

  print even_googlers, " ", even_surp, " ", odd_googlers, " ", odd_surp

  answer = even_googlers + odd_googlers

  if num_surp >= even_surp + odd_surp:
    addval = even_surp + odd_surp 
  else: addval = num_surp

  answer = answer + addval

  output(numtest, answer)
        

def main():
  numtests = int(f_in.readline())

  for i in range(1, int(numtests) + 1):
    runtest(i)
    print "Test Case #",i," done"

  f_in.close()
  f_out.close()

main()
