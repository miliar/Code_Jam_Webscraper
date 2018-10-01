import sys

def solution(f):
  lines = [f.readline() for _c in range(5)]
  n = int(lines[0])
  a = set(lines[n].split())
  lines = [f.readline() for _c in range(5)]
  n = int(lines[0])
  b = set(lines[n].split())
  a.intersection_update(b)
  if len(a) == 0:
	return "Volunteer cheated!"
  if len(a) == 1:
	return a.pop()
  return "Bad magician!"

f = sys.stdin
T = int(f.readline())
for x in range(T):
  print "Case #%d: "%(x+1) + solution(f)
