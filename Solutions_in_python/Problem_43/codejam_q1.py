import string, sys

numbers = string.digits + string.ascii_lowercase
print numbers

input_file = sys.argv[1]
f = open(input_file, 'r')

T = int(f.readline())
print T

cases = [f.readline().strip() for i in range(T)]

f.close()

fw = open('codejam_q1.out', 'w')
i = 0
for case in cases:
  i += 1
  j = 0
  l = []
  for c in case:
    if c not in l:
       l.append(c)
  base = len(l)
  if len(l) == 1:
    base = 2
  s = ''
  for c in case:
    s += numbers[l.index(c)]
  # can't start with 0 -> replace 0 and 1
  s = s.replace('0', '#').replace('1', '0').replace('#', '1')
  print case, ' -> ', s
  sum = 0
  for j, sc in enumerate(s[::-1]):
    sum += numbers.index(sc) * (base ** j)
  
  print 'Case #%d: %d' % (i, sum)
  fw.write('Case #%d: %d\n' % (i, sum))

fw.close()
