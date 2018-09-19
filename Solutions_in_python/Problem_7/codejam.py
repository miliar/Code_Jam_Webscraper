import sys
from math import *
from decimal import *

getcontext().prec=100

global caseid
caseid = 1

def out(x):
	sys.stdout.write(str(x))

def cr():
	out('\n')

def hd():
	global caseid
	out('Case #%d: ' % caseid)
	caseid += 1
	
def db(x):
	sys.stderr.write(str(x))

def rl(conv=None):
	return map(conv, sys.stdin.readline().strip().split())

def rt(conv=None):
	s = sys.stdin.readline().strip()
	if conv == None:
		return s
	else:
		return conv(s)

