import sys

def solve(infile, outfile):
  num_tests = int(infile.readline().strip())
  for test_num in range(num_tests): 
    num_blocks = int(infile.readline().strip())
    naomi_blocks = [float(x) for x in infile.readline().strip().split(" ")]
    ken_blocks = [float(x) for x in infile.readline().strip().split(" ")]
    naomi_blocks = sorted(naomi_blocks)
    ken_blocks = sorted(ken_blocks)
    k2 = num_blocks-1
    k1 = 0
    n1 = 0
    while k1 <= k2: 
      if naomi_blocks[n1] > ken_blocks[k1]: 
        k1 += 1
      else:
        k2 -= 1
      n1 += 1
    deceit_score = k1
    n1 = num_blocks -1
    k2 = num_blocks-1
    k1 = 0
    while k1 <= k2: 
      if naomi_blocks[n1] > ken_blocks[k2]: 
        k1 += 1
      else:
        pop_index = k2
        for i in range(k1, k2): 
          if ken_blocks[i] > naomi_blocks[n1]: 
            pop_index = i
        ken_blocks.pop(pop_index)
        k2 -= 1
      n1 -= 1
    war_score = k1
    outfile.write("Case #%d: %d %d\n" % (test_num+1, deceit_score, war_score))

if __name__ == "__main__": 
  filename = sys.argv[1]
  with open(filename, "r") as infile: 
    with open(filename + ".out", "w") as outfile:
      solve(infile, outfile)
  print("Done!")
