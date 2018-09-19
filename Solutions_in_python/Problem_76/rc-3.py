
import string
import re



s = raw_input()
num_r = int(s)
c_num = 0
for r in xrange(num_r):
  c_num +=1
  s = raw_input()
  candy_num = int(s)
  s = raw_input()
  cvl = s.split()

  minv = int(cvl[0])
  xv = 0
  tv = 0
  for v in cvl:
    v = int(v)
    minv = min(minv, v)
    xv ^= v
    tv += v


  p_list = []
  p_list.append("Case #")
  p_list.append(str(c_num))
  p_list.append(": ")
  if xv == 0: 
    p_list.append(str(tv-minv))
  else:
    p_list.append("NO")


  print ''.join(p_list)



