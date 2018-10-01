def ints():
  return map(int, input().split())

num_cases, = ints()

for case_num in range(1, num_cases + 1):
  N,S,p,*t = ints()
  t.sort()
  t.reverse()
  y=sum((x>=(3*p-2)) and (x>=p) for x in t)
  z=sum((3*p-4) <= x < (3*p-2)  and (x>=p) for x in t[y:y+S])

  print("Case #%d: %d" % (case_num, y+z))
