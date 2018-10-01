#!/usr/bin/env python

def findFirst(mood, cooktop, start, end):
  for i in range(start, end+1):
    if cooktop[i] == mood:
      return i
  return -1

def flip(cooktop, start, k):
	for i in range(start, start+k):
		cooktop[i] = not cooktop[i]

def big_flipper(cooktop, k):
  counter = 0
  cooktop_last = len(cooktop)-1
  i = findFirst(False,cooktop,0,cooktop_last)
  if i == -1:
    return 0
  if i + k > len(cooktop):
      return -1
  while i + k  <= len(cooktop) and i!=-1:
    print "i=",i
    flip(cooktop, i, k)
    print cooktop
    counter = counter + 1
    i=findFirst(False, cooktop, i+1, cooktop_last)
    print "i=",i
    if i + k > len(cooktop):
      return -1
  return counter


def main():
  case_num = 0
  output = []
  biglist = readInput("A-small-attempt2.in")
  # biglist = readInput("sample.txt")
  for cooktop, k in biglist:
    print "----------------------------", case_num+1, "----------------------------"
    print cooktop,k
    counter = big_flipper(cooktop,k)
    print "counter=",counter
    output.append(counter)
    case_num+=1
  writeOutput(output, "tmp.txt")

  # # cooktop=[False, False, False, True, False, True, True, False]
  # # cooktop=[True, True, True, True, True]
  # # cooktop=[False, True, False, True, False]
  # cooktop = [True, False, True]
  # k=2
  # print cooktop
  # print "cooktop len =", len(cooktop)
  # counter = big_flipper(cooktop,k)
  # print "counter=",counter


def readInput(filename):
	biglist=[]
 	with open(filename) as file:
 		next(file)
 		for line in file:
 			pancakes=[]
 			s, k = line.strip().split()
 			for c in s:
 				if c == '+':
 					pancakes.append(True)
 				else:
 					pancakes.append(False)
 			biglist.append([pancakes,int(k)])
 	return biglist

def writeOutput(output, filename):
	file = open(filename, "w")
	for i in range(0,len(output)):
		if output[i] == -1:
			file.write("Case #%d: IMPOSSIBLE\n" % (i+1))
		else:
			file.write("Case #%d: %s\n" % (i+1, output[i]))
	file.close()

if __name__ == "__main__":
    main()