#
# Google Code Jam 2009
# Watershed
#
# Problem
# 
# Geologists sometimes divide an area of land into different regions
# based on where rainfall flows down to. These regions are called 
# drainage basins.
# 
# Given an elevation map (a 2-dimensional array of altitudes), labels
# the map such that locations in the same drainage basin have the same
# label, subject to the following rules.
# 
#     * From each cell, water flows down to at most one of its 4
#       neighboring cells.
#     * For each cell, if none of its 4 neighboring cells has a lower
#       altitude than the current cell's, then the water does not flow,
#       and the current cell is called a sink.
#     * Otherwise, water flows from the current cell to the neighbor
#       with the lowest altitude.
#     * In case of a tie, water will choose the first direction with
#       the lowest altitude from this list: North, West, East, South.
# 
# Every cell that drains directly or indirectly to the same sink is part
# of the same drainage basin. Each basin is labeled by a unique lower-case
# letter, in such a way that, when the rows of the map are concatenated 
# from top to bottom, the resulting string is lexicographically smallest.
# (In particular, the basin of the most North-Western cell is always
# labeled 'a'.)
# 
# Input
# 
# The first line of the input file will contain the number of maps, T.
# T maps will follow, each starting with two integers on a line -- H and
# W -- the height and width of the map, in cells. The next H lines will
# each contain a row of the map, from north to south, each containing W
# integers, from west to east, specifying the altitudes of the cells.
# 
# Output
# 
# For each test case, output 1+H lines. The first line must be of the form
# 
# Case #X:
# 
# where X is the test case number, starting from 1. The next H lines
# must list the basin labels for each of the cells, in the same order
# as they appear in the input.
# 
# Limits
# 
# T = 100;
# 
# Small dataset
# 
# 1 = H, W = 10;
# 0 = altitudes < 10.
# There will be at most two basins.
# 
# Large dataset
# 
# 1 = H, W = 100;
# 0 = altitudes < 10,000.
# There will be at most 26 basins.
# 
# Sample
# 
# Input
# 
# 5
# 3 3
# 9 6 3
# 5 9 6
# 3 5 9
# 1 10
# 0 1 2 3 4 5 6 7 8 7
# 2 3
# 7 6 7
# 7 6 7
# 5 5
# 1 2 3 4 5
# 2 9 3 9 6
# 3 3 0 8 7
# 4 9 8 9 8
# 5 6 7 8 9
# 2 13
# 8 8 8 8 8 8 8 8 8 8 8 8 8
# 8 8 8 8 8 8 8 8 8 8 8 8 8
#
#
# Output
#
# Case #1:
# a b b
# a a b
# a a a
# Case #2:
# a a a a a a a a a b
# Case #3:
# a a a
# b b b
# Case #4:
# a a a a a
# a a b b a
# a b b b a
# a b b b a
# a a a a a
# Case #5:
# a b c d e f g h i j k l m
# n o p q r s t u v w x y z
# 
# Notes
# 
# In Case #1, the upper-right and lower-left corners are sinks. Water
# from the diagonal flows towards the lower-left because of the lower 
# altitude (5 versus 6).
# 

def readMap(file):
  """
    Read a map from the file.

    H W
    (grid of altitudes)
  """

  retval = {}

  firstLine = file.readline()
  firstLine = firstLine.strip(' \t\n')
  parts = firstLine.split(' ')

  H = int(parts[0])
  W = int(parts[1])

  retval['H'] = H
  retval['W'] = W
  retval['map'] = []
  retval['watershed'] = []
  retval['sinks'] = []

  for i in range(H):
    line = file.readline()
    line = line.strip(' \t\n')
    parts = line.split(' ')

    retval['map'].append([])
    retval['watershed'].append([])

    for j in range(W):
      retval['map'][i].append(int(parts[j]))
      retval['watershed'][i].append(-1)

#  print retval['map']
  return retval

def readFile(filename):
  """
    Read an input file.

    NMaps
    <map>
    <map>
    <map>
    ...

  """

  retval = []

  with open(filename, "rt") as file:
    firstLine = file.readline()
    firstLine = firstLine.strip(' \t\n')
    nmaps = int(firstLine)

    for i in range(nmaps):
      map = readMap(file)

      if map:
        retval.append(map)

  return retval

def calculateWatershedFor(map, x, y):
  """
    Find the watershed for the given position.
  """

  if map['watershed'][y][x] >= 0:
    return map['watershed'][y][x]

  # find lowest
  min = map['map'][y][x]
  minx = x
  miny = y
  different = False

  # If we compare them N-W-E-S, then in the case
  # of ties, we'll prefer the answer in the correct
  # order

  # North
  if y > 0:
    if map['map'][y-1][x] < min:
      min = map['map'][y-1][x]
      minx = x
      miny = y-1
      different = True

  # West
  if x > 0:
    if map['map'][y][x-1] < min:
      min = map['map'][y][x-1]
      minx = x-1
      miny = y
      different = True

  # East
  if x < (map['W'] - 1):
    if map['map'][y][x+1] < min:
      min = map['map'][y][x+1]
      minx = x+1
      miny = y
      different = True

  # South
  if y < (map['H'] - 1):
    if map['map'][y+1][x] < min:
      min = map['map'][y-1][x]
      minx = x
      miny = y+1
      different = True

  if not different:
    # We're a sink
    map['sinks'].append( [x, y, ''] )
    map['watershed'][y][x] = len(map['sinks']) - 1
  else:
    # Our sink the the same as the lowest
    # NOTE:  Recursion is probably bad
    map['watershed'][y][x] = calculateWatershedFor(map, minx, miny)

  return map['watershed'][y][x]

def buildWatersheds(map):
  """
    Fills in the ['sinks'] with a set
    of watersheds (x, y, letter).

    Fills in the ['watershed'] map with the
    index of the corresponding watershed.

    Calculates the watershed letters.
  """

  for x in range(map['W']):
    for y in range(map['H']):
      calculateWatershedFor(map, x, y)

  # allocate sink letters
  letters = "abcdefghijklmnopqrstuvwxyz"
  i = 0

  # Assign letters based on order (left-right, top-bottom)
  for y in range(map['H']):
    for x in range(map['W']):
      s = map['watershed'][y][x]
      sink = map['sinks'][s]

      if not sink[2]:
        sink[2] = letters[i]
        i = i + 1

def displayWatershedMap(map):
  """
    Print out the watershed map
  """

  for row in map['watershed']:
    line = ""
    for col in row:
      line = line + map['sinks'][col][2] + " "

    line = line.strip()
    print line

def process(data):
  """
    Run the test.
  """

  i = 1
  for map in data:
    buildWatersheds(map)
    print "Case #%d:" % (i, )
    displayWatershedMap(map)
    i = i + 1

#data = readFile('watershed-sample.in')
#data = readFile('B-small-attempt0.in')
data = readFile('B-large.in')
process(data)
