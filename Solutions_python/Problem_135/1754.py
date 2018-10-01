#!/usr/bin/python
import sys, os

class Grid:
  def __init__(self, row, rows):
    self.row = row
    self.rows = rows

  def __repr__(self):
    output_str = "%d\n" % self.row
    for row in self.rows:
      output_str += "%d %d %d %d\n" % (row[0], row[1], row[2], row[3])
    return output_str

class TestCase:
  def __init__(self, grids):
    if len(grids) != 2:
      raise Exception("Should be only 2 grids")
    self.grids = grids
  
  def __repr__(self):
    output_str = ''
    for i, grid in enumerate(self.grids):
      output_str += "Grid %d :\n" % (i+1)
      output_str += "%s\n" % str(grid)
    return output_str

  def result(self):
    row1 = self.grids[0].rows[self.grids[0].row-1]
    row2 = self.grids[1].rows[self.grids[1].row-1]
    elements = []
    for val1 in row1:
      for val2 in row2:
        if val1 == val2:
          elements.append(val1)
          break
    if len(elements) > 1:
      return "Bad magician!"
    elif len(elements) == 0:
      return "Volunteer cheated!"

    return "%d" % elements[0]


def read_test_cases(input_filename):
  test_cases = []
  with open(input_filename) as input_file:
    lines = input_file.read().split("\n")
  num_test_cases = lines[0]
  
  for i in range(1, len(lines), 10):
    if len(lines[i].replace(" ", '')) == 0:
      continue
    row1 = int(lines[i])
    grid_1_rows = []
    grid_1_rows.append(map(int, lines[i+1].split()))
    grid_1_rows.append(map(int, lines[i+2].split()))
    grid_1_rows.append(map(int, lines[i+3].split()))
    grid_1_rows.append(map(int, lines[i+4].split()))

    row2 = int(lines[i+5])
    grid_2_rows = []
    grid_2_rows.append(map(int, lines[i+6].split()))
    grid_2_rows.append(map(int, lines[i+7].split()))
    grid_2_rows.append(map(int, lines[i+8].split()))
    grid_2_rows.append(map(int, lines[i+9].split()))

    test_cases.append(TestCase([Grid(row1, grid_1_rows), Grid(row2, grid_2_rows)]))

  
  return test_cases

def usage():
  print "Usage: a_magic_trick.py input_file"

def main():
  if len(sys.argv) != 2:
    usage()
    sys.exit(1)

  input_filename = os.path.abspath(sys.argv[1])
  test_cases = read_test_cases(input_filename)

  for i, test_case in enumerate(test_cases):
    print "Case #%d: %s" % (i+1, test_case.result())

if __name__ == "__main__":
  main()
