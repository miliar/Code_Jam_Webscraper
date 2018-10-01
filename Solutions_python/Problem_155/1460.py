import sys

#fin = open("test1.in","r")
fin = open("A-large.in","r")
t = fin.readline().rstrip()
# print t
for i in range(0,int(t)):
	tmp = fin.readline().rstrip().split(' ')
	smax = int(tmp[0])
	s = list(tmp[1])
	s = [int(x) for x in s]
	active = 0
	add = 0
	for j in range(0, smax+1):
		# print j
		if active < j:
			add += j - active
			active = j
		active += s[j]
	# print smax, s
	print "Case #" + str(i+1) + ": " + str(add)

