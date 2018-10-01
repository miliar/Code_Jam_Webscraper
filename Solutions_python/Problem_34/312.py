import re

f = open('./A-large.in', 'r')
ldn = f.readline()
ldna = ldn.split(' ')
l = int(ldna[0])
d = int(ldna[1])
n = int(ldna[2])

words = []
for i in range(d):
  words.append(f.readline().replace('\n', ''))

cases = []
for i in range(n):
  cases.append(f.readline().replace('\n', '').replace(r'(', r'[').replace(r')', r']'))

for i in range(n):
  cnt = 0
  for j in range(d):
    if re.match(cases[i] , words[j]):
      cnt += 1
  print 'Case #' + str(i + 1) + ': ' + str(cnt)

