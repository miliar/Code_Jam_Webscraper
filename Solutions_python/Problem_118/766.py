fairs = [
1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004,
100000020000001,
100220141022001,
102012040210201,
102234363432201,
121000242000121,
121242363242121,
123212464212321,
123456787654321,
400000080000004
]

def isPalindrome(n):
  s = str(n)
  for i in range(0, len(s)/2):
    if s[i] != s[-i - 1]:
      return False
  return True

def findThem():
  palindromes = set()
  fairs = set()
  fairs.add(1)
  a = 2
  while a < 10e7:
    if isPalindrome(a):
      b = a * a;
      if isPalindrome(b):
        fairs.add(b)
        print b
    a = a + 1
  f = open('fairs', 'w')
  for i in fairs:
    f.write('%d' % i);
  f.close()

def search(start, end):
  t = 0
  for x in fairs:
    if x < start:
      continue
    if x > end:
      break
    t = t + 1
  return t

def main():
  f = open('C-large-1.in', 'r')
  o = open('output.txt', 'w')
  n = int(f.readline())
  _n = 1
  while _n <= n:
    line = f.readline().split()
    start = int(line[0])
    end = int(line[1])
    result = search(start, end)
    o.write('Case #%d: %d\n' % (_n, result))
    _n = _n + 1
  o.close()
  f.close()

main()
