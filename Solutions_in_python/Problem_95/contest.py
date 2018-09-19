import sys

googlerese = ['ejp mysljylc kd kxveddknmc re jsicpdrysi','rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','de kr kd eoya kw aej tysr re ujdr lkgc jv']
translated =['our language is impossible to understand','there are twenty six factorial possibilities','so it is okay if you want to just give up']

codex = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm' , '\n':'\n' , 'q':'z' , 'z':'q'}

q = open('small.txt','r')
a = open('a.txt','w')
translate = ''
c = 0
for line in q:
	c+=1
	#print line
	translate = ''
	l = list(line)
	#print 'a'
	for i in range(len(l)):
		if l[i] == ' ':
			translate += ' '
			#print 'match'
		elif codex.has_key(l[i]):
			translate += codex[l[i]]
		else:
			print line
			print translate
				
	a.write("Case #"+str(c)+": "+translate)
	#print translate

q.close()
a.close()


	
