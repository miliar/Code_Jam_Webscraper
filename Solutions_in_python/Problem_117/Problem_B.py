import string

# _file = open("D:/Dropbox/Projects/CodeJAM/2013 Qualification Round/Problem_B/data.txt")
# _file = open("D:/Dropbox/Projects/CodeJAM/2013 Qualification Round/Problem_B/B-small-attempt0.in")
_file = open("D:/Dropbox/Projects/CodeJAM/2013 Qualification Round/Problem_B/B-large.in")
_result = open("D:/Dropbox/Projects/CodeJAM/2013 Qualification Round/Problem_B/result.txt", "w")

def checkField(matrix, rows, cols):
  if rows <=1 or cols <= 1:
    return 'YES'

  for x in range(0, rows):
    for y in range(0, cols):
      if matrix[x][y] < max(matrix[x]) and matrix[x][y] < max(map(lambda row: row[y], matrix)):
        return 'NO'

  return 'YES'

dataset_size = int(_file.readline())

for case in range(0, dataset_size):
  # print _file.readline().split()
  x, y = map(lambda value: int(value), _file.readline().split())
  
  matrix = [[0 for _y in xrange(y)] for _x in xrange(x)]

  # populate matrix with data
  for row in range(0, x):
    matrix[row] = map(lambda value: int(value), _file.readline().split())

  # print matrix

  _result.write("Case #" + str(case + 1) + ": " + checkField(matrix, x, y) + "\n")

  # print checkField(matrix, x, y)

_file.close()
_result.close()