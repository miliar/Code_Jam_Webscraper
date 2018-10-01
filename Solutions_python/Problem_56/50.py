import sys
import time
import re
import pprint

try:
	import psyco
	psyco.full()
except ImportError:
	pass

class tee: 
	def __init__(self, *fds):
		self._fds = fds
	
	def write(self, data):
		for fd in self._fds:
			fd.write(data)

	def flush(self):
		for fd in self._fds:
			fd.flush()
	
	def close(self):
		for fd in self._fds:
			fd.close()
	
def fileCaseReader(source):
	entryCount = int(source.readline().strip())
	for i in range(1, entryCount + 1):
		yield i

def readLines(source):
	entryCount = int(source.readline().strip())
	for i in range(0, entryCount):
		yield source.readline()

def readLineOfInts(f):
	return map(int, f.readline().strip().split(" "))
	
def gravity(line, N):
	line = line.replace(".", "")
	return "." * (N - len(line)) + line
	
def runCase(f):
	N, K = readLineOfInts(f)
	lines = [gravity(f.readline().strip(), N) for i in range(N)]
	translines = [''.join([lines[i][j] for i in range(N)]) for j in range(N)]
	diag1lines = [[] for i in range(N*2)]
	diag2lines = [[] for i in range(N*2)]
	for i in range(N):
		for j in range(N):
			diag1lines[i+j] += lines[i][j]
			diag2lines[i+N-j-1] += lines[i][j]
	diag1lines = [''.join(l) for l in diag1lines]
	diag2lines = [''.join(l) for l in diag2lines]
	red, blue = False, False
	for l in lines:
		if 'R' * K in l:
			red = True
		elif 'B' * K in l:
			blue = True
	for l in translines:
		if 'R' * K in l:
			red = True
		elif 'B' * K in l:
			blue = True
	for l in diag1lines:
		if 'R' * K in l:
			red = True
		elif 'B' * K in l:
			blue = True
	for l in diag2lines:
		if 'R' * K in l:
			red = True
		elif 'B' * K in l:
			blue = True
	if red and blue:
		print "Both"
	elif red:
		print "Red"
	elif blue:
		print "Blue"
	else:
		print "Neither"

def timerWrap(f):
	def __inner(*args,**kwargs):
		start = time.time()
		try:
			return f(*args, **kwargs)
		finally:
			print >> sys.stderr, "Runtime: %.3f sec" % (time.time() - start)
	return __inner

#@timerWrap
def main():
	f = file("rotate.in", "r");
	sys.stdout = tee(sys.stdout, file("rotate.out", "w"))
	for index in fileCaseReader(f):
		print "Case #%d:" % index,
		runCase(f)
		sys.stdout.flush()

main()
