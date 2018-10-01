#! usr/bin/python

file_object = open("A-small-attempt1.in", "r")
file_write = open("A-small-output.out", "w")
num = int(file_object.readline())
for i in range(num): #number of cases
  for j in range(2): #two inputs for each
    answer = int(file_object.readline())
    array = []
    for k in range(4): #make array
      array.append(file_object.readline().split())
    if j == 0: #if first array, save the row
      choice = array[answer - 1]
    else: #if second, save the second row
      row = array[answer - 1]
      ans = [x for x in choice if x in row]
      if len(ans) == 1:
        file_write.write("Case #{0}: {1}\n".format(i + 1, ans[0]))
      elif len(ans) == 0:
        file_write.write("Case #{0}: Volunteer cheated!\n".format(i + 1))
      else:
        file_write.write("Case #{0}: Bad magician!\n".format(i + 1))

file_object.close()