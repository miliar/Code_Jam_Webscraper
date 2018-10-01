# magic trick

# declare constants
ROWS = 4
COLS = 4

# declare and initialize data structures and variables
square1 = [[0 for x in range(COLS)] for y in range(ROWS)]
square2 = [[0 for x in range(COLS)] for y in range(ROWS)]

try:
  # open files
  #fin = open("a.in", 'r')
  fin = open("A-small-attempt1.in", 'r')
  #fout = open("a.out", 'w')
  fout = open("A-small-attempt1.out", 'w')
  
  # read number of test cases
  T = int(fin.readline())

  # loop for number of test cases
  for case in range(T):
    # read first answer
    ans1 = int(fin.readline())
    
    # read first arrangement
    for i in range(ROWS): 
      line = fin.readline()
      square1[i] = line.split()
    #print(square1)

    # read second answer
    ans2 = int(fin.readline())

    # read second arrangement
    for i in range(ROWS): 
      line = fin.readline()
      square2[i] = line.split()
    #print(square2)

    # get first answer row
    ansrow1 = square1[ans1-1]
    #print(ansrow1)
      
    # get second answer row
    ansrow2 = square2[ans2-1]
    #print(ansrow2)

    # process magic and output result
    count = 0
    for entry1 in ansrow1:
      for entry2 in ansrow2:
        #print(entry1 + ' ' + entry2)
        if entry1 == entry2:
          count += 1
          magic = entry1
    #print(count)

    if count == 1:
      fout.write("Case #" + str(case+1) + ": " + magic + "\n")
    elif count == 0:
      fout.write("Case #" + str(case+1) + ": Volunteer cheated!\n")
    else:
      fout.write("Case #" + str(case+1) + ": Bad magician!\n")
          
  # close files
  fin.close()
  fout.close()

except IOError:
  print("Cannot read from and/or write to file.")  
