from cjlib.input import *
from cjlib.runner import TaskRunner, DummyRunner
import logging, math

logging.basicConfig(level=logging.DEBUG)

def isPalin(i):
	i = str(int(i))
	s = len(i)/2
	return i[:s] == i[::-1][:s]

def genPalin(start,end):
	for i in xrange(start,end+1):
		if isPalin(i):
			base = math.sqrt(i)
			if base%1.0 == 0.0:
				if(isPalin(base)):
					yield i
	raise StopIteration

def process(case):
	case = [int(x) for x in case]
	o=0
	for notused in genPalin(case[0],case[1]):
		#print notused
		o+=1
	return o

get("""3
1 4
10 120
100 1000""")

r = TaskRunner(process, DummyRunner)

while neof():
	r.add(line().split(" "))

r.run(True)