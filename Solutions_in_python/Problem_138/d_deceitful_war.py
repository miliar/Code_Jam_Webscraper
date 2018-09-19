#!/usr/bin/python
import sys, os, copy

class Player:
  def __init__(self, blocks):
    self.blocks = blocks

  def __repr__(self):
    output_str = ''
    for block in self.blocks:
      output_str += "%.3f " % block

    return output_str

class TestCase:
  def __init__(self, naomi_blocks, ken_blocks):
    self.naomi_blocks = naomi_blocks
    self.ken_blocks = ken_blocks
  
  def __repr__(self):
    output_str = 'Naomi: %s\nKen: %s' % (self.naomi_blocks, self.ken_blocks)
    
    return output_str

  def get_deceptive_wins(self):
    # First stage, remove Ken's largest blocks
    naomi_blocks = copy.copy(self.naomi_blocks.blocks)
    ken_blocks   = copy.copy(self.ken_blocks.blocks)
    naomi_blocks.sort()
    ken_blocks.sort()
    naomi_score = 0
    #print 'naomi blocks: ', naomi_blocks
    #print 'ken   blocks: ', ken_blocks
    start_j = len(ken_blocks)-1
    for i in range(len(naomi_blocks)-1, -1, -1):
      for j in range(start_j, -1, -1):
        if ken_blocks[j] < naomi_blocks[i]:
          naomi_score += 1
          start_j = j - 1
          break
    return naomi_score

  def get_normal_wins(self):
    # First stage, remove Ken's largest blocks
    naomi_blocks = copy.copy(self.naomi_blocks.blocks)
    ken_blocks   = copy.copy(self.ken_blocks.blocks)
    naomi_blocks.sort()
    ken_blocks.sort()
    naomi_score = 0
    for i, n_weight in enumerate(naomi_blocks):
      found_greater = False
      for j in range(len(ken_blocks)):
        if ken_blocks[j] > n_weight:
          found_greater = True
          break
      if found_greater:
        ken_blocks = ken_blocks[:j] + ken_blocks[j+1:]

      else:
        ken_blocks = ken_blocks[1:]
        naomi_score += 1

    return naomi_score


  def result(self):
    return self.get_deceptive_wins(), self.get_normal_wins()

def read_test_cases(input_filename):
  test_cases = []
  with open(input_filename) as input_file:
    lines = input_file.read().split("\n")
  num_test_cases = lines[0]
  
  for i in range(1, len(lines), 3):
    if len(lines[i].replace(" ", '')) == 0:
      continue
    num_blocks = int(lines[i])
    naomi_blocks = Player(map(float, lines[i+1].split()))
    ken_blocks   = Player(map(float, lines[i+2].split()))
    test_cases.append(TestCase(naomi_blocks, ken_blocks))

  
  return test_cases

def usage():
  print "Usage: d_deceitful_war.py input_file"

def main():
  if len(sys.argv) != 2:
    usage()
    sys.exit(1)

  input_filename = os.path.abspath(sys.argv[1])
  test_cases = read_test_cases(input_filename)

  for i, test_case in enumerate(test_cases):
    deceptive_wins, normal_wins = test_case.result()
    print "Case #%d: %d %d" % (i+1, deceptive_wins, normal_wins)

if __name__ == "__main__":
  main()
