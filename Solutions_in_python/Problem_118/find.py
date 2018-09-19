fout = open("Square1.txt",'w')

import operator
def lrange(num1, num2 = None, step = 1):
    op = operator.__lt__
    if num2 is None:
        num1, num2 = 0, num1
    if num2 < num1:
        if step > 0:
            num1 = num2
        op = operator.__gt__
    elif step < 0:
        num1 = num2
    while op(num1, num2):
        yield num1
        num1 += step
        
def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

import math
for i in lrange(2,10**7):
    a = str(i)
    if a == a[::-1]:
        i = int(a)
        sq = i * i
        a = str(sq)
        if a == a[::-1]:
            print a    
            fout.write("%i,"%(int(sq)))