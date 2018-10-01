from collections import Counter

"""


"""
keys = Counter()
chests = []
totalOpen = 0
results = []
states = set()

def loot(chest):
  global keys, chests, totalOpen, results
  assert(not chest.open)
  assert(keys[chest.type] > 0)
  keys[chest.type] -= 1
  for x in chest.keys:
    keys[x] += 1
  chest.open = True
  results.append(str(chest.id))
  totalOpen += 1

def pushState():
  global keys, chests, totalOpen, results, states
  state = 0
  for x in chests:
    if x.open:
      state |= 1 << x.id
  if state in states:
    return False
  states.add(state)
  if len(states) % 50000 == 0:
    print len(states), state
  return True

def popState(chest):
  global keys, chests, totalOpen, results
  for x in chest.keys:
    keys[x] -= 1
    assert(keys[x] >= 0)
  chest.open = False
  keys[chest.type] += 1
  totalOpen -= 1
  results.pop()

def solve():
  global keys, chests, totalOpen, results, states
  if totalOpen == len(chests):
    return True
  if not pushState():
    return False
  for x in chests:
    if not x.open and keys[x.type] > 0:
      loot(x)
      if totalOpen == len(chests):
        return True
      if solve():
        return True
      popState(x)
  return False

class Chest:
  def __init__(self, t, id):
    self.keys = []
    self.open = False
    self.type = t
    self.id = id
  def __repr__(self):
    return "%d" % self.open
  def toStr(self):
    return "[%d, %d, %d, %s]" % (self.id, self.open, self.type, self.keys)

def main():
  global keys, chests, totalOpen, results, states
  f = open('D-small-attempt1.in', 'r')
  o = open('output.txt', 'w')
  n = int(f.readline())
  _n = 1
  while _n <= n:
    keys = Counter()
    chests = []
    totalOpen = 0
    results = []
    states = set()

    line = f.readline().split()
    numKeys = int(line[0])
    numChests = int(line[1])
    line = f.readline().split()
    for x in line:
      keys[int(x)] += 1

    for i in range(numChests):
      line = f.readline().split()
      t = int(line[0])
      numKeys = int(line[1])
      newChest = Chest(t, i + 1)
      for j in range(2, 2 + numKeys):
        newChest.keys.append(int(line[j]))
      assert(numKeys == len(newChest.keys))
      chests.append(newChest)

    print "Solving case: %d, %d, %d" % (_n, len(list(keys.elements())), numChests)
    print keys, chests
    # import cProfile
    # pr = cProfile.Profile()
    # pr.enable()
    r = solve()
    # pr.disable()
    # pr.print_stats()
    if r:
      result = ' '.join(results)
    else:
      result = "IMPOSSIBLE"
    print result

    o.write('Case #%d: %s\n' % (_n, result))
    _n = _n + 1
  o.close()
  f.close()

main()