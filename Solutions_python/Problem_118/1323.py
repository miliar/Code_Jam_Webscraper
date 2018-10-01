import math

f = open('C-small-attempt0.in', 'r')
fo = open('C-small.out', 'w')
def ip():
  #return raw_input()
  global f
  return f.readline()

def op(st):
  #print st
  #return
  global fo
  fo.write(st + "\n")
  
num_cases = int(ip())

def is_palindrome(num):
  st = str(num)
  start = 0
  end = len(st)-1
  while start < end:
    if st[start] != st[end]:
      return False
    start += 1
    end -= 1
  return True

for case in xrange(num_cases):
  start, end = [int(num) for num in ip().split(" ")]
  start = int(math.ceil(math.sqrt(start)))
  end = int(math.sqrt(end))
  count = 0
  for num in xrange(start, end+1):
    if is_palindrome(num):
      sqr = num * num
      if is_palindrome(sqr):
        count += 1
  op("Case #%d: %d" % (case+1, count))