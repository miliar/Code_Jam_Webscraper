
translate = dict()
enc = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
dec = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
for i in range(len(enc)):
	translate[enc[i]] = dec[i]
translate['q'] = 'z'
translate['z'] = 'q'

#for c in "abcdefghijklmnopqrstuvwxyz":
#	if c not in translate.keys():
#		print "Manca "+c

fin = open('input.txt', 'r')
num = int(fin.readline())
for i in range(num):
	line = [int(x) for x in fin.readline().split()]
	n = line[0]
	s = line[1]
	p = line[2]
	scores = line[3:]
	res = 0
	scores.sort(reverse=True)
	
	for score in scores:
		t = int(score/3)
		r = score%3
		
		if r == 0 and t >= p:
			res += 1
			continue
		
		if r > 0 and t+1 >= p:
			res += 1
			continue
		
		if s > 0 and t > 0:
			if r == 0 and t+1 >= p:
				s -= 1
				res += 1
				continue
			if r == 1:
				continue
			if r == 2 and t+2 >= p:
				s -= 1
				res += 1
				continue

		break
	print "Case #%d: %d" % (i+1, res)

