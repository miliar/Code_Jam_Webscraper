with open("inputmagic.txt") as f:
  l = [a.strip() for a in f.readlines()]

testcases = int(l.pop(0))

def getintersection(a):
  v1 = int(a[0])
  v2 = int(a[5])

  s1 = set(a[v1].split())
  s2 = set(a[5 + v2].split())

  i = s1.intersection(s2)
  if len(i) == 0:
    return "Volunteer cheated!"
  elif len(i) == 1:
    return i.pop()
  else:
    return "Bad magician!"


for i in range(1, testcases+1):
  inter = getintersection(l)
  l = l[10:]
  print "Case #{}: {}".format(i, inter)
