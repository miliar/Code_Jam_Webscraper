import itertools

def readfile(filename):
  """
    Read the file.

    N
    P Q
    P Q
    P Q
    ...
  """

  retval = {}

  with open(filename, "rt") as file:
    N = int(file.readline().strip())
    retval['N'] = N
    retval['cases'] = []

    for i in range(N):
      P,Q = [ int(x) for x in file.readline().strip().split() ]
      case = {'P':P, 'Q':Q}
      case['list'] = [ int(x) for x in file.readline().strip().split() ]
      retval['cases'].append(case)

  return retval

def maxLessThan(list, n):
  """
    Return the biggest number in the list less
    than n.
  """

  max = None

  for i in list:
    if (not max) and (i < n):
      max = i
    elif (i > max) and (i < n):
      max = i

  return max

def minGreaterThan(list, n):
  """
    Return the smallest number in the list bigger
    than n.
  """

  min = None

  for i in list:
    if (not min) and (i > n):
      min = i
    elif (i < min) and (i > n):
      min = i

  return min

def calculateBribe(P, Qlist):
  """
    Calculate the bribe needed for releasing prisioners
    in the order provided by Qlist.
  """

  empties = []
  retval = 0

  for c in Qlist:
    emptiesNearby = [ maxLessThan(empties, c), minGreaterThan(empties, c) ]
    if not emptiesNearby[0]:
      emptiesNearby[0] = 0
    if not emptiesNearby[1]:
      emptiesNearby[1] = P+1

    below = c - emptiesNearby[0] - 1
    above = emptiesNearby[1] - c - 1
    retval = retval + below + above

#    print "%d: %d - %d: %d (%d, %d)" % (c, below, above, retval, emptiesNearby[0], emptiesNearby[1])
    empties.append(c)

  return retval

def handleTestCase(case):
  """
    Run a test case.
  """

  P = case['P']
  Q = case['Q']
  list = case['list']

  perms = itertools.permutations(list)

  min = 0

  for Qlist in perms:
#    print Qlist
    bribe = calculateBribe(P, Qlist)

    if not min:
      min = bribe
    elif bribe < min:
      min = bribe

  return min

def process(data):
  """
    Process the file data.
  """

  i = 1
  for case in data['cases']:
    bribe = handleTestCase(case)

    print "Case #%d: %d" % (i, bribe)
    i = i + 1

process(readfile("C-small-attempt0.in"))
