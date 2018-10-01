#
# Author: Cheng-Shih, Wong (code14)
# Email:  mob5566@gmail.com
#

from __future__ import print_function

t = int(raw_input())

for ti in xrange(1, t+1):
  ac, aj = map(int, raw_input().split())

  act = []
  tt = [0]*2

  for i in xrange(ac):
    s, e = map(int, raw_input().split())
    act.append([s, e, 0])
    tt[0] += e-s

  for i in xrange(aj):
    s, e = map(int, raw_input().split())
    act.append([s, e, 1])
    tt[1] += e-s

  act.sort(key=lambda x: x[0])
  act.append([act[0][0]+1440, act[0][1]+1440, act[0][2]])

  changed = True

  while changed:
    changed = False

    sl = 2000

    for i in xrange(len(act)-1):
      if act[i][2] == act[i+1][2]:
        dl = act[i+1][0]-act[i][1]

        if dl < sl and dl+tt[act[i][2]]<=720:
          changed = True
          sl = dl
          si = i

    if changed:
      tt[act[si][2]] += sl
      act[si][1] = act[si+1][1]
      act.remove(act[si+1])

  ans = 0

  for i in xrange(len(act)-1):
    if act[i][2] == act[i+1][2]:
      ans += 2
    else:
      ans += 1  

  print("Case #{}: {}".format(ti, ans))
