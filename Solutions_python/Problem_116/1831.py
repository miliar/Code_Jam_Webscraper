
win = ['XXXX', 'TXXX', 'XTXX', 'XXTX', 'XXXT', 
'OOOO', 'TOOO', 'OTOO', 'OOTO', 'OOOT']

def readFile(filename):
	f = file(filename)
	count = int(f.readline())
	print count
	contents = f.readlines()
	ret = []
	for i in xrange(count):
		ret.append([c for s in contents[i*5: i*5+4] for c in s.strip()])
	return ret


if __name__ == '__main__':
	cs = readFile('A-large.in.txt')
	o = file('r.txt', 'w')
	for j,a in enumerate(cs):
		# print a
		r = []
		for i in xrange(4):
			r.append(''.join(a[i*4:i*4+4]))
		for i in xrange(4):
			r.append(''.join(a[i::4]))
		r.append(''.join([a[0], a[5], a[10], a[15]]))
		r.append(''.join([a[3], a[6], a[9], a[12]]))
		for i,rr in enumerate(r):
			# print rr, i
			if rr in win:
				o.write('Case #'+str(j+1)+': '+str(not rr[0]=='T' and rr[0] or rr[1])+' won\n')
				break
		if i==9 and not r[9] in win:
			if '.' in a:
				o.write('Case #'+str(j+1)+': Game has not completed\n')
			else:
				o.write('Case #'+str(j+1)+': Draw\n')
	o.close()



