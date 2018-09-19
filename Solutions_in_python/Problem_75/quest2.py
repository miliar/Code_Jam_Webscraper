num_cases = int(raw_input())
tricks= []
for case_num in xrange(0, num_cases):
  tricks.append(raw_input().split())

Elements = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']

case = 0
for case_num in tricks:
  compound = {}
  C = int(case_num[0])
  for i in xrange(0, C):
    compound[case_num[i+1][0]+case_num[i+1][1]] = case_num[i+1][2]
    compound[case_num[i+1][1]+case_num[i+1][0]] = case_num[i+1][2]
  d = 1+C
  D = int(case_num[d])
  radioactive = []
  for i in xrange(0, D):
    radioactive.append(case_num[d+i+1][0]+case_num[d+i+1][1])
  n = d + D + 2
  N = case_num[n]
  mylist = []
  for letter in N:
    length = len(mylist)
    if length == 0:
      mylist.append(letter)
    else:
      if letter + mylist[length-1] in compound:
        old = mylist.pop()
        mylist.append(compound[letter+old])
      else:
        #good we can add it to the list
        mylist.append(letter)
      for i in radioactive:
        if len(mylist) != 0:
          if (i[0] == mylist[len(mylist)-1] and i[1] in mylist) or (i[1] == mylist[len(mylist)-1] and i[0] in mylist):
            mylist = []
  case +=1
#for case_num in xrange(1, num_cases + 1):
  print "Case #%d: [%s]" % (case, ", ".join(mylist))
#  print "Case #",case_num[0],": " , mylist
