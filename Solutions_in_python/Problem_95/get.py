dic = {}
for i in range(3):
	s = raw_input()
	t = raw_input()
	for i in range(len(s)):
		dic[s[i]] = t[i]
#print dic, len(dic)
x = input()
for q in range(x):
	s = raw_input()
	t = ""
	for i in range(len(s)):
		t += dic[s[i]]
	print "Case #"+str(q+1)+":",t

