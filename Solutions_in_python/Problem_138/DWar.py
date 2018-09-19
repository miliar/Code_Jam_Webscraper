#!/usr/bin/env python
import copy

def find_bigger_than(l,n):
	for x in l:
		if x>n:
			return x
	return False

def find_bigger_than_from_back(l,n):
	for x in l[::-1]:
		if x>n:
			return x
	return False
	
def war(nw,kw,num):
	nwp = 0
	while num>0:
		t = find_bigger_than(kw,nw[0])
		nw.remove(nw[0])
		if t:
			kw.remove(t)
		else:
			kw.pop(-1)
			nwp += 1
		num -= 1	
	return nwp

def dwar(nw,kw,num):
	nwp = 0
	while num>0:
		t = find_bigger_than(kw,nw[0])
		if t:
			kw.remove(t)
			nw.pop(-1)
		else:
			t2 = find_bigger_than_from_back(nw,kw[-1])
			nw.remove(t2)
			kw.pop(-1)
			nwp += 1
		num -= 1
	return nwp	


n = int(raw_input())
for i in range(n):
	num = int(raw_input())
	nw = sorted(map(float,raw_input().strip().split()),reverse=True)
	kw = sorted(map(float,raw_input().strip().split()),reverse=True)
	ncw = copy.copy(nw)
	kcw = copy.copy(kw)
	print "Case #"+str(i+1)+": "+str(dwar(nw,kw,num))+" "+str(war(ncw,kcw,num))
