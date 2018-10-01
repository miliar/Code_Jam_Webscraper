# During code jam competition, this code was running under
# Mac OS X 10.6.7 2011 MacBook Pro, pypy 1.5.0-alpha0 GCC 4.0.1
# Python 2.7.1 measured 250946 pystones/sec
import threading, time, sys, re, math
from itertools import combinations
inData = open(sys.argv[1]).read().strip()
#inData = """1
#2
#5 5"""
def noobAdd(x, y):
	if y > x:
		x2 = y
		y2 = x
		y = y2
		x = x2
	x = bin(x).split("b")[1][::-1]
	y = bin(y).split("b")[1][::-1]
	out = ""
	for k,v in enumerate(x):
		try:
			d = int(v) + int(y[k])
			if d >= 2: d = 0
		except IndexError:
			d = int(v)
		out += str(d)
	out = out[::-1]
	return int(out, 2)
class Awesome(threading.Thread):
	def __init__(self, i):
		threading.Thread.__init__(self)
		self.i = i
		self.done = False
		self.st = time.time()
		self.out = "NO"
	def run(self):
		data = map(lambda x: int(x), self.i.split(" "))
		maxValue = reduce(lambda x,y:x+y, data)
		aVal = []
		if len(data) == 2:
			if data[0] == data[1]:
				self.out = data[0]
		for i in range(int(math.ceil(len(data)//2)), len(data)-1):
			p = combinations(data, i+1)
			for x in p:
				notIn = filter(lambda o: o not in x, data)
				notIn = data[:]
				for z in x:
					if z in notIn:
						del notIn[notIn.index(z)]
				if len(notIn) == 0: continue
				patrick = reduce(lambda o,p: noobAdd(o, p), notIn)
				patrickCnt = reduce(lambda o,p: noobAdd(o, p), x)
				if patrickCnt != patrick:
					continue # reject
				elif len(x) > len(notIn):
					sean = reduce(lambda o,p: o+p, x)
					aVal.append(sean)
		if len(aVal) > 0:
			self.out = max(aVal)
		self.done = time.time()

"""no = 1
for k,i in enumerate(inData.split("\n")[1:]):
	sys.stderr.write(str(no)+"\r")
	if len(i.split(" ")) == 1:
		continue
	th = Awesome(i)
	th.run()
	print "Case #%s: %s" % (no, th.out)
	no += 1
exit()"""
th = []
for i in inData.split("\n")[1:]:
	if len(i.split(" ")) == 1:
		continue
	th.append(Awesome(i))
	th[-1].start()
	sys.stderr.write(str(len(th))+"\r")
sys.stderr.write("\nThread assigned\n")
for k,i in enumerate(th):
	while True:
		if i.done:
			print "Case #%s: %s" % (k+1, i.out)
			#if k == 2:
			#	print i.stackturn
			break
for i in th:
	sys.stderr.write("%s finished in %s\n"%(i.name, i.done - i.st))
