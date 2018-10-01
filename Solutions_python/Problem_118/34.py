import sys
import bisect

b0 = set()
b = set()

def pal(x):
  return x == x[::-1]

def add(x):
  x = int(x)
  if pal(str(x * x)):
    b0.add(x)
    b.add(x * x)

def go(s, i, cnt1, cnt2):
  if i == 1 and s[-1] == '0':
    return
  if i > 0:
    add(s + s[::-1])
    add(s[:-1] + s[::-1])
  if i == 25:
    return
  if cnt1 >= 5: return
  if cnt2 >= 2: return
  for t in {'0', '1', '2'}:
    go(s + t, i + 1, cnt1 + (t == '1'), cnt2 + (t == '2'))
  
def get(n):
  return bisect.bisect_right(a, n)

go('', 0, 0, 0)
add('3')
a = sorted(b)
a0 = sorted(b0)
for x in a:
  print(x)
