#!/usr/local/bin/python

# GOOGLE CODE JAM
# This is a submission to the Google Code Jam 2013


import sys
import os
import re
import math

#####################################################################
####                        SETTINGS                             ####
#####################################################################


#bool - Defines wether test mode should be used regardless of arguments
        # Useful for debugging in an IDE, make sure to set it back
FORCE_TEST_MODE = False

#str - Test Input 
      #Just like a real code jam File
      #maybe put the sample input in a file 
      #and read it here
TEST_INPUT = open("tidynumbers.in","rU").read()

#list - Expected utputs for each test case
        #Without Case #x: 
        #make sure len of this == number of problems in input
TEST_OUTPUT=map(lambda x: x[x.find(": ")+2:], open("tidynumbers.out","rU").read().split("\n"))
#bool - Defines wether the number of lines per test case is constant or not
        #This will be stated in the problem description
        #If false, you need to have a look at parseInput
NR_OF_LINES_PER_CASE_ISCONSTANT = True

#int - Number of lines per case, if NR_OF_LINES_PER_CASE_ISCONSTANT = True
      #Most of the times this is 1 if not otherwise stated int the problem desc
NR_OF_LINES_PER_CASE = 1



#####################################################################
####                        YOUR CODE HERE                       ####
#####################################################################



#Parses the input file 
#ONLY EXECUTED if not NR_OF_LINES_PER_CASE_ISCONSTANT
#input = list of string with lines in the input file excluding the first
#problemCount = Ammount of problems in input "first line"

#Returns list of list of strings of test cases
def parseInput(input, problemCount):
  #Example Implementation:
  #   one line at the beginning of every
  #   problem with an int that represents
  #   the number of lines per problem

  cases = []
  for x in xrange(0,problemCount):
    count = input[0]
    curCase = []
    for line in xrange(0,int(count)+1):
      curCase.append(input.pop(0))
    cases.append(curCase)
  return cases







#Main problem solving

#case = list of string with lines in input file
#       that belong to one Test case
#Returns output for the case as string; Unformatted (no Case: #X)
#   and without \n
def solveCase(case):
  i = int(case[0])
  return str(tidy(i))


def tidy(i):
  cp = i
  curpos = 0
  while True:
    number_string = str(i)[0:len(str(cp))-curpos]
    rest = str(i)[len(str(cp))-curpos:]
    prev = 0
    newstr = ""
    count = 0

    for ch in number_string:
      digit = int(ch)
      if not prev <= digit:
        break
      prev = digit
      count += 1
    if count == len(number_string):
      rest = "9"*len(rest)
      return int(number_string+rest)

    #find latest thats larger
    digit = int(number_string[count])
    k = 0
    c = 0
    for d in number_string:
      newstr += d
      k+=1
      if int(d) > digit:
        c = k
    i = int(str(int(newstr[:c] + zeroes(len(number_string) - c)) - 1) + rest)
    curpos += 1


def zeroes(i):
  res = ""
  for x in xrange(0,i):
    res += "0"
  return res

    

######################################################################
#####ONLY BOILERPLATE CODE BELOW - SHOULD NOT NEED TO BE ALTERED #####
######################################################################


def getCases(lines):
  # Parse file
  cases = []
  try:
    m = int(lines.pop(0)) #Number of problems always in line 
  except Exception, e:
    errorOut("Invalid Input")


  if NR_OF_LINES_PER_CASE_ISCONSTANT:
    n = NR_OF_LINES_PER_CASE
    i = 0

    for x in xrange(0,m):
      case = []
      for x in xrange(0,n):
          case.append(lines.pop(0))
      cases.append(case)

  else:
    cases = parseInput(lines,m)

  print "Found "+str(len(cases))+" test cases\n"
  return cases



## Work with unit tests - define TEST_INPUT : see above
def test():
  
  if not TEST_INPUT or not TEST_OUTPUT:
    errorOut("Please make sure you define TEST_INPUT and TEST_OUTPUT")
  testcount = len(TEST_OUTPUT)
  rightcount = 0
  

  cases = getCases(TEST_INPUT.split("\n"))
  solutions = TEST_OUTPUT

  if not len(cases) == testcount:
    errorOut("Invalid test cases")

  i=0
  for testcase in cases:
    toprint = "Evaluating: "
    solve = solveCase(testcase)
    if solve==solutions[i]:
      toprint += "Correct!"
      rightcount+=1
    else:
      toprint+="Uh oh!"
    
    toprint += "   Given: "+solve
    toprint += " Expected: "+solutions[i]
    toprint += " Input: "+ "\\n".join(testcase)
    print toprint 

    i+=1

  print
  print "Solved "+str(rightcount)+" out of "+ str(testcount) + " test cases correctly"



def production():
  # Get filename
  #Default filename = SCRIPT.in (Without .py)  
  filename = sys.argv[0][:-3]+".in"
  if "--in" in sys.argv:
    try:
      filename=sys.argv[sys.argv.index("--in")+1]
    except Exception, e:
      errorOut("Please specify an input file")
    

  if not os.path.isfile(filename):
    errorOut("Specified input file does not exist\nStandard input: "+sys.argv[0][:-3]+'.in\n')

  # Get output file
  out=sys.argv[0][:-3]+".out"
  if "--out" in sys.argv:
    try:
      out=sys.argv[sys.argv.index("--out")+1]
    except Exception, e:
      errorOut("Please specify an output file")
    
  
  # Get input by line
  f=None
  try:
    f=open(filename,"rU")
  except Exception, e:
    errorOut("Could not open input file!")

  cases = getCases(f.read().split("\n"))


  
  # Let's play

  output = ""
  curCase = 1
  for case in cases:
    print "Solving " + str(curCase) + " out of "+str(len(cases))
    output+="Case #"+str(curCase)+": "
    output+=solveCase(case)
    output+="\n"
    curCase+=1
 

  # Store output
  try:
    outf = open(out,"w")
    outf.write(output)
    outf.close()

    print "\n\n"

    print "Done! Output stored in: "+out
  except Exception, e:
    print "Error writing output! Here it is in stdout \n"+output

def main():
  if "--test" in sys.argv or FORCE_TEST_MODE:
    print "Test mode"
    test()
  else:
    print "Production mode"
    production()
    


#Exit with error
def errorOut(msg):
  sys.stderr.write(msg+"\n")
  sys.exit(1)

if __name__ == '__main__':
  main()
