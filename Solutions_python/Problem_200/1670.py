def test(i):
  st = str(i)
  prev = st[0]
  for i in st[1:]:
    if i >= prev:
      prev = i
      continue
    else:
      return False
  return True
  
def testList(lis):
  prev = lis[0]
  for i in lis[1:]:
    if i >= prev:
      prev = i
      continue
    else:
      return False
  return True
  
def bruteforce(i):
  while not test(i):
    i -= 1
  return i

def dropZeros(lis):
  i = 0
  while lis[i] == '0':
    i += 1
  return lis[i:]

def solution(i):
  st = list(str(i))
  curr = []
  while curr != st:
    curr = st[:]
    setNines = False
    for i in range(1, len(st)):
      if setNines:
        continue
      if (st[i-1] > st[i]):
        st[i-1] = chr(ord(st[i-1]) - 1)
        setNines = True
        for j in range(i, len(st)):
          st[j] = '9'
  return ''.join(dropZeros(st))
      

t = int(input())
for i in range(1, t + 1):
  n = int(input())
  print("Case #{}: {}".format(i, solution(n)))
  