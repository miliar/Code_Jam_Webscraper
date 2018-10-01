file1 = open("input.txt", "r")
file2 = open("output.txt", 'w')

T = file1.readline()

def testCase(currentT):
      row1 = "hi"
      row2 = "hi"
      number = -1
      count = 0
      
      targetRow = file1.readline()
      for i in range(4):
            if i==int(targetRow)-1:
                  row1 = file1.readline().split()
            else:
                  file1.readline()
                  
      targetRow = file1.readline()                 
      for i in range(4):
            if i==int(targetRow)-1:
                  row2 = file1.readline().split()
            else:
                  file1.readline()

      for item in row1:
            if item in row2:
                  number = item
                  count+=1

      print (row1)
      print (row2)
      
      if (number != -1 and count==1):
            return (str("Case #"+str(currentT) + ": " + str(number)+"\n"))
      elif (number == -1):
            return (str("Case #"+str(currentT) + ": Volunteer cheated!\n"))
      elif (count > 0):
            return (str("Case #"+str(currentT) + ": Bad magician!\n"))
      else:
            return ("Something wnet wrong")

for i in range(int(T)):
      file2.write(testCase(i+1))

file1.close()
file2.close()
