import re

f = open('A-large.in', 'r')
content = f.read()
content = content.splitlines()
out = open("large-A-out", 'w')
number = int(content[0])
count = 0

def flip(s):
	return '+' if s == '-' else '-'

for l in content:
	if count == 0:
		count += 1
		continue
	ss = l.split(' ')
	s = ss[0]
	num = int(ss[1])
	least = 0
	for i in range(len(s)-num+1):
		if s[i] == '-':
			least += 1
			for j in range(i, i + num):
				s = s[0:j] + flip(s[j]) + s[j+1:]
	if '-' in s:
		out.write('Case #' + str(count) + ': IMPOSSIBLE\n')
	else:
		out.write('Case #' + str(count) + ': ' + str(least) + '\n')
	count += 1
