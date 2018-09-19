import sys

class Robot:
  def __init__(self, buts, tag):
    self.buts = buts
    self.tag = tag
    self.pos = 1
    self.index = 0
    self.get_next()

  def get_next(self):
    res = 0
    for i in xrange(self.index+1, len(self.buts)):
      if self.buts[i][0] == self.tag:
        res = i
        break

    self.index = res

  def update(self, changed):
    buts = self.buts
    if self.index:
      cur_but = buts[self.index]
      if self.pos < cur_but[1]:
        self.pos += 1
      elif self.pos > cur_but[1]:
        self.pos -= 1
      elif not changed and self.buts[self.index-1][2]:
        changed = True
        cur_but[2] = True
        self.get_next()

#    print self.tag, self.pos, self.buts[self.index]

    return changed

  def has_finished(self):
    return (self.index == 0)

def solve(buts):
  bot_o = Robot(buts, 'O')
  bot_b = Robot(buts, 'B')

  i = 0
  while (not bot_o.has_finished()) or (not bot_b.has_finished()):
    changed = False
    changed = bot_o.update(changed)
    changed = bot_b.update(changed)
    i += 1
#    print '----'

  return i

#f = open('p1-1inp.txt')
f = sys.stdin
T = int(f.readline())
for i in xrange(0, T):
  line = f.readline().split()[::-1]
  N = int(line.pop())
  buts = [('X', -1, True)]

  for j in xrange(0, N):
    buts.append([line.pop(), int(line.pop()), False])

#  print buts
  res = solve(buts)
  print "Case #%d: %d" % (i+1, res)
