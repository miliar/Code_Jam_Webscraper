#!/usr/bin/python3
T = int(input())

def prop(n):
  res = False
  t = str(n)

  f = int(t[0])
  for i in t[1:]:
    w = int(i)
    if(f > w):
      return False

    f = w

  return True



for i in range(T):
  x = int(input())

  if(x < 10):
    print("Case #{}: {}".format(i+1,x))
    continue

  res = False
  while res is not True:
    res = prop(x)
    x -= 1

  print("Case #{}: {}".format(i+1,x+1))
