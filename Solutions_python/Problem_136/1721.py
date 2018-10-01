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
  def __init__(self, c, f, x):
    self.c = c
    self.f = f
    self.x = x
  
  def __repr__(self):
    output_str = '%.7f %.7f %.7f' % (self.c, self.f, self.x)
    return output_str

  def get_optimal_time(self):
    cur_fastest_time = self.x/2.0
    for num_farms in range(0, 2000):
      rate = 2.0
      time_to_purchase_farms = 0.0
      for j in range(1, num_farms + 1):
        time_to_purchase_farms += self.c/rate
        rate = 2.0 + self.f * j
      total_time =  self.x /rate + time_to_purchase_farms
      if total_time < cur_fastest_time:
        cur_fastest_time = total_time
    return cur_fastest_time

  def result(self):
    return self.get_optimal_time()

def read_test_cases(input_filename):
  test_cases = []
  with open(input_filename) as input_file:
    lines = input_file.read().split("\n")
  num_test_cases = lines[0]
  
  for i in range(1, len(lines)):
    if len(lines[i].replace(" ", '')) == 0:
      continue
    data = map(float, lines[i].split())
    c = data[0]
    f = data[1]
    x = data[2]

    test_cases.append(TestCase(c, f, x))

  
  return test_cases

def usage():
  print "Usage: b_cookie_clicker.py input_file"

def main():
  if len(sys.argv) != 2:
    usage()
    sys.exit(1)

  input_filename = os.path.abspath(sys.argv[1])
  test_cases = read_test_cases(input_filename)

  for i, test_case in enumerate(test_cases):
    print "Case #%d: %.7f" % (i+1, test_case.result())

if __name__ == "__main__":
  main()
