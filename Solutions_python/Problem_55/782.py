import sys
import psyco
from collections import deque
psyco.full()

def ReadInts():
  return list(map(int, sys.stdin.readline().strip().split(" ")))

def ReadInt():
  return int(sys.stdin.readline().strip())


T = ReadInt()
for _ in xrange(T):
  income = 0
  R, k, N = ReadInts()
  q = deque(ReadInts())
  riding = deque([])
  while R > 0:
    emptySeats = k
    while q and q[0] <= emptySeats:
      group = q.popleft()
      income += group
      emptySeats -= group
      riding.append(group)
    while riding:
      q.append(riding.popleft())
    R -= 1
  print "Case #%d: %d" %(_+1,income)

