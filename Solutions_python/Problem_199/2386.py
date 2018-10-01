from collections import Counter as cc

def all_happy(s):
  x= [y for y in s]
  c= cc(x)
  if len(c)==1 and '+' in c:
    return True
  return False
  
def flips(s, k):
  x= [y for y in s]
  i, cnt = 0, 0
  while i<= len(x)-k:
    if x[i]=='-':
      cnt+=1
      for j in range(i, i+k):
        x[j]= '-' if x[j]== '+' else '+'
    i+=1
  if all_happy(''.join(x)):
    return cnt
  else:
    return -1
  
t= int(input())
for i in range(1, t+1):
  s, k= map(str, input().split())
  k= int(k)
  if all_happy(s):
    print('Case #{}: {}'.format(i, 0))
    continue
  if k> len(s):
    print('Case #{}: {}'.format(i,'IMPOSSIBLE'))
    continue
  f= flips(s, k)
  if f== -1:
    print('Case #{}: {}'.format(i,'IMPOSSIBLE'))
    continue
  else:
    print('Case #{}: {}'.format(i, f))
  
  
  
  
  