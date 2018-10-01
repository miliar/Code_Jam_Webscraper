#
# Author: Cheng-Shih, Wong (code14)
# Email:  mob5566@gmail.com
#

from __future__ import print_function

t = int(raw_input())

for ti in xrange(1, t+1):
  n, r, o, y, g, b, v = map(int, raw_input().split())

  ans = ''

  rr = r-g
  bb = b-o
  yy = y-v
  nn = rr+bb+yy

  R = (['RG'*g+'R'] if g else [])+['R']*(rr-(1 if g else 0))
  B = (['BO'*o+'B'] if o else [])+['B']*(bb-(1 if o else 0))
  Y = (['YV'*v+'Y'] if v else [])+['Y']*(yy-(1 if v else 0))

  if (g==0 or rr>0) and (o==0 or bb>0) and (v==0 or yy>0) and \
     nn>=rr*2 and nn>=bb*2 and nn>=yy*2:

    if rr >= bb and rr>=yy:
      H = R
      if bb>=yy:
        M = B
        L = Y
      else:
        M = Y
        L = B
    elif bb>=rr and bb>=yy:
      H = B
      if rr>=yy:
        M = R
        L = Y
      else:
        M = Y
        L = R
    else:
      H = Y
      if bb>=rr:
        M = B
        L = R
      else:
        M = R
        L = B

    hi = mi = li = 0
    hh = len(H)
    mm = len(M)
    ll = len(L)

    last = 0
    ans += H[0]
    hi += 1
    hh -= 1

    while hh>0 or mm>0 or ll>0:
      if last==0:       # H
        if mm >= ll:
          ans += M[mi]
          mi += 1
          mm -= 1
          last = 1
        else:
          ans += L[li]
          li += 1
          ll -= 1
          last = 2
      elif last==1:     # M
        if hh >= ll:
          ans += H[hi]
          hi += 1
          hh -= 1
          last = 0
        else:
          ans += L[li]
          li += 1
          ll -= 1
          last = 2
      else:             # L
        if mm > hh:
          ans += M[mi]
          mi += 1
          mm -= 1
          last = 1
        else:
          ans += H[hi]
          hi += 1
          hh -= 1
          last = 0
  elif (r==g and (r+g)==n) or \
       (b==o and (b+o)==n) or \
       (y==v and (y+v)==n):
    if r:
      ans = 'RG'*r
    elif b:
      ans = 'BO'*b
    else:
      ans = 'YV'*y
  else:
    ans = 'IMPOSSIBLE'

  
  print("Case #{}: {}".format(ti, ans))
