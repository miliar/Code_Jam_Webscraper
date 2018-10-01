import sys
from string import ascii_lowercase as basins

class Finder():
  def __init__(self, H, W, rows):
    self.H = H
    self.W = W
    self.rows = rows

  def min_altitude_neighbour(self, row, col):
    if H == 1 and W == 1: # only one cell,
      return (row, col)   # return self
    l = []
    pos = []
    if row != 0: # N
      l.append(rows[row - 1][col])
      pos.append((row - 1, col))
    if col != 0: # W
      l.append(rows[row][col - 1])
      pos.append((row, col - 1))
    if col != self.W - 1: # E
      l.append(rows[row][col + 1])
      pos.append((row, col + 1))
    if row != self.H - 1: # S
      l.append(rows[row + 1][col])
      pos.append((row + 1, col))
    i = l.index(min(l))
    if l[i] >= rows[row][col]: # min neighbour alt is higher than own alt,
      return (row, col)        # return self
    return pos[i]

input_file = sys.argv[1]
f = open(input_file, 'r')

T = int(f.readline())
print 'T = %d' % T

fw = open('codejam_q2.out', 'w')
for i in range(T):
  H, W = (int(x) for x in f.readline().split())
  #print 'H = %d, W = %d' % (H, W)
  rows = [[int(x) for x in f.readline().split()] for j in range(H)]
  #print rows
  flow = [[None for x in range(W)] for j in range(H)]

  finder = Finder(H, W, rows)
  current_index = 0
  
  for row in range(H):
    for col in range(W):
      if not flow[row][col]:
        r, c = row, col
        current_basin = []
        while True:
          #print r, c
          flows_to_row, flows_to_col = finder.min_altitude_neighbour(r, c)
          current_basin.append((r, c))
          if (flows_to_row, flows_to_col) == (r, c): # sink
            #print 'Sink: ', r, c
            break
          r, c = flows_to_row, flows_to_col
          if flow[r][c]: # we got to an existing flow, no need to follow it
            break
        if flow[r][c]:
          # mark all in current_basin as that sink
          for p in current_basin:
            flow[p[0]][p[1]] = flow[r][c]
        else:
          # mark all in current_basin with new letter
          for p in current_basin:
            flow[p[0]][p[1]] = basins[current_index]
          current_index += 1
        #print flow

  print 'Case #%d:' % (i + 1)
  fw.write('Case #%d:\n' % (i + 1))
  for flow_row in flow:
    #print ' '.join(flow_row)
    fw.write(' '.join(flow_row) + '\n')

fw.close()
f.close()
