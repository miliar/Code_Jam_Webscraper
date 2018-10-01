import sys

l = list('abcdefghijklmnopqrstuvwxyz')
k = list('yhesocvxduiglbkrztnwjpfmaq')

n = raw_input()
o = []
for i in range(int(n)):
	s = ""
	x = raw_input()
	for i in x:
		if i != ' ':
			s += k[l.index(i)]
		else: s += ' '
	o.append(s)

for i in range(int(n)):
	print "Case #" + str(i+1) + ':', o[i]
