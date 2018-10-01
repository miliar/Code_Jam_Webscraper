data = []
num_friends = []

def file_io():
  fo = open("A-small-attempt0.in")
  first_line = fo.readline()
  for i in xrange(int(first_line)):
    num_friends.append(0)
    line = fo.readline()
    all_things = line.split()
    data.append(all_things[1])
  fo.close()

def add_friend(i):
  string = data[i]
  incremented = int(string[0]) + 1
  data[i] = str(incremented) + string[1:]

def test(i):
  total_num = 0
  for char in data[i]:
    total_num += int(char)
  num_up =  0
  for j in xrange(len(data[i])):
    if num_up >= j:
      num_up += int(data[i][j])
  return num_up == total_num

def main():
  file_io()

  for i in xrange(len(data)): # loop through all test cases
    while True:
      if test(i):
        break
      add_friend(i)
      num_friends[i] += 1

  f = open("A-small-attempt0.out", "w")
  for i in xrange(len(num_friends)):
    f.write("Case #" + str(i+1) + ": " + str(num_friends[i]) + "\n")
  f.close()

main()
