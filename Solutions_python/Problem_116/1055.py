import math
import time
start_time = time.time()

filename = 'A-large'
def gettics():
  fp = open('%s.in' % filename, 'r')
  n = fp.readline().strip('\r\n')
  c = 0
  ticlist = []
  xtics = []
  otics = []
  ct = 0
  for line in fp:
    tics = line.strip('\r\n')
    if not len(tics):
      continue
    i = 1 + (c * 4)
    for ch in tics:
      if ch in ['X', 'T']:
        xtics.append(i)
      if ch in ['O', 'T']:
        otics.append(i)
      if ch == 'T':
        ct += 1
      i += 1

    c += 1
    if c % 4 == 0:
      ticlist.append([xtics, otics, ct])
#      print xtics, otics
      xtics = []
      otics = []
      c = 0
      ct = 0
  return ticlist

def whowin(lst):
  wins = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
          [1, 5, 9, 13],
          [2, 6, 10, 14],
          [3, 7, 11, 15],
          [4, 8, 12, 16],
          [1, 6, 11, 16],
          [4, 7, 10, 13]]
  winning = []
  i = 0
  for l in lst:
    tempx = set(l[0])
    tempo = set(l[1])
#    print '-----', l
    for win in wins:
      win = set(win)
#      print win.intersection(tempx)
      if len(win.intersection(tempx)) == 4:
        i += 1
        winning.append('Case #%s: %s' % (i, 'X won'))
        break
      elif len(win.intersection(tempo)) == 4:
        i += 1
        winning.append('Case #%s: %s' % (i, 'O won'))
        break
    else:
#        print len(l[0]) + len(l[1]), l[2]
        if len(l[0]) + len(l[1]) - l[2] == 16:
          i += 1
          winning.append('Case #%s: %s' % (i, 'Draw'))
        else:
          i += 1
          winning.append('Case #%s: %s' % (i, 'Game has not completed'))
  return winning
      
xy = gettics()
#print xy
xy = whowin(xy)
#print xy
fp = open('%s_out.txt' % filename, 'w')
fp.write('\n'.join(xy))
fp.close()
print time.time() - start_time, "seconds"
