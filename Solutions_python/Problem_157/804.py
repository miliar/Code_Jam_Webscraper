import os
import sys
from pprint import pprint

#matrix = {3:{3:-1,7:11,11:-7},7:{3:-11,7:-1,11:3},11:{3:7,7:-3,11:-1}}
matrix = {"i":{"i":"-","j":"k","k":"-j"},
          "j":{"i":"-k","j":"-","k":"i"},
          "k":{"i":"j","j":"-i","k":"-"}
          }

def mult(a,b):
    return matrix[a][b]

def main():
  filePtr = open("in.in",'r')
  fileLines = filePtr.readlines()
  fileLines = [x.rstrip('\n') for x in fileLines]
  filePtr.close()

  noOfTest = fileLines[0]

  c = 1
  j = 0
  while(j<int(noOfTest)):
    inp  = fileLines[c].split(" ")
    repitition = inp[1]
    pattern = list(fileLines[c+1])
    pattern = pattern*int(repitition)
    #pprint(pattern)


    positive = True
    found_i = False
    found_j = False
    found_k = False
    found = False
    if ''.join(pattern) == "ijk":
      found_i = found_j = found_k = True
      found = True
    while len(pattern):
      if found:
          break
      
      #print "!!!"
      #pprint(pattern[:4])
      #print "##len", len(pattern)
      if len(pattern)>1:
          a = pattern[0]
          b = pattern[1]
          ret = mult(a,b)
          pattern = pattern[2:]
      else:
          ret = ''
      #print "!!!"
      #pprint(pattern)
      if ret:
          if positive and ret[0] == '-':
              positive = False
          elif not positive and ret[0] == '-':
              positive = True
          if ret[0] == '-':
              if len(ret) == 2:
                ret = ret[1]
              else:
                  ret = ''

      if ret:
          pattern.insert(0,ret)

      if not len(pattern):
         break

      if pattern[0] == 'i' and not found_i:
          found_i = True
          pattern = pattern[1:]
      elif found_i and pattern[0] == 'j' and not found_j:
          found_j = True
          pattern = pattern[1:]
      elif found_j and pattern[0] == 'k' and not found_k:
          found_k = True
          pattern = pattern[1:]
      elif (len(pattern) == 1):
          if found_k and pattern[0] != '':
              found_k = False
          pattern = pattern[1:]



    #print positive,found_i,found_j,found_k
    sys.stdout.write("Case #")
    sys.stdout.write(str(j+1))
    print ":",
    if positive and  found_i and found_j and found_k:
        print "YES"
    else:
        print "NO"
    c = c +2
    j = j + 1


# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()
