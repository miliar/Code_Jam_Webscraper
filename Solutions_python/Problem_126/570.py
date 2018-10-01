import math
import re

f = open('b.txt', 'r')
out = open('b-output.txt', 'w')
total = int(f.readline())

def cal(h,n):
	count = 0
	h = h.replace("a"," ")
	h = h.replace("e"," ")
	h = h.replace("i"," ")
	h = h.replace("o"," ")
	h = h.replace("u"," ")
	h = h.split(" ")
	for abc in h:
		if len(abc) >= n:
			return 1
	return 0

for tt in range(total):
	#t = map(int,f.readline().split(" "))
	t = f.readline().split(" ")
	n = int(t[1])
	s = t[0]
	count = 0
	
	for a in range(len(s)-n+1):
		for b in range(n,len(s[a:])+1):
			#if a+b <= len(s):
			sub = s[a:][:b]
			cc=0
			if cal(sub,n):
				#print sub + "      "+ str(a) + "     " + str(a+b)
				count = count + 1

	print count
	out.write("Case #" + str(tt+1) + ": " + str(count) + "\n")

