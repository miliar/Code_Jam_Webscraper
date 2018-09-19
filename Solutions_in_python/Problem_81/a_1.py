import sys
import string

def wlcount(string):
	return string.count('0'), string.count('1')
def getline():
	return sys.stdin.readline()[:-1]
def myfilter(table, mylist):
	newlist = []
	for i in range(len(table)):
		if table[i] != '.':
			newlist.append(mylist[i])
	return newlist
def avg(mylist):
	ret = 0.0
	for a in mylist:
		ret += a
	return ret / len(mylist)

def testcase():
	n = int(getline())
	table = []
	for i in range(n):
		table.append(getline())
	wl = []
	for i in range(n):
		tmpwl = []
		for j in range(n):
			rate1, rate2 = wlcount(table[i][:j]+table[i][j+1:])
			tmpwl.append(rate2 / (0.0 + rate1 + rate2))
		wl.append(tmpwl)
	owl = []
	for i in range(n):
		wllist = []
		for j in range(n):
			if table[i][j] != '.':
				wllist.append(wl[j][i])
		owl.append(avg(wllist))
	oowl = []
	for i in range(n):
		oowl.append(avg(myfilter(table[i], owl)))
	for i in range(n):
		print 0.25 * wl[i][i] + 0.50 * owl[i] + 0.25 * oowl[i]

t = int(getline())
for i in range(t):
	print 'Case #{0}:'.format(i+1)
	testcase()

