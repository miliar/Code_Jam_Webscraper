import sys

VERBOSE = False

if __name__ == "__main__":
  input = open(sys.argv[1])
  input.readline() # Number of cases
###  goal = "abc"
  goal = "welcome to code jam"
  goalset = set(goal)
  for casenum, test in enumerate(input):
    test = test.strip()
    grid = [[0]*len(test) for i in goal]

    # Set up grid - (-1)*number of same letters previous in goal word
    for entry, letter in enumerate(goal):
      for i in xrange(len(goal)-1):
        continue
        grid[entry][i] = -goal[:entry].count(letter)

    for i, letter in enumerate(test):
      for entry in xrange(len(goal)):
        if i > 0:
          grid[entry][i] = grid[entry][i-1]
      if letter in goalset:
        for pos, l in enumerate(goal):
          if l == letter:
            grid[pos][i] = grid[pos-1][i]+grid[pos][i-1] if pos-1 >= 0 else grid[pos][i-1]+1
    if VERBOSE:
      print '  '*2 + '   '.join(test)
      for i, line in enumerate(grid):
        print goal[i], ' '.join(["%3d" % x for x in line])
      print "=-=-=-="*4
    n = "0000" + "%04d" % grid[-1][-1]
    print "Case #%d: %s" % (casenum+1, n[-4:])

