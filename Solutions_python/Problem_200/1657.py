#!/usr/bin/python

T = int(input())
for t in range(T):
	s = input()
	s2 = [s[0]]
	for i in range(1, len(s)):
		if s2[-1] <= s[i]:
			s2.append(s[i])
		else:
			c = len(s) - i
			s2[-1] = chr(ord(s2[-1])-1)
			while len(s2) > 1 and s2[-1] < s2[-2]:
				s2.pop()
				s2[-1] = chr(ord(s2[-1])-1)
				c += 1
			s2.extend(['9'] * c)
			break

	while s2[0] == '0':
		del s2[0]

	r = ''.join(s2)
	print("Case #" + str(t+1) + ': ' + r)
