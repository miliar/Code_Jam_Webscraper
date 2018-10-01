#!/usr/bin/python3
# -*- coding: utf-8 -*-


def tokenize(s):
	return [ x.strip() for x in ((s.replace('(', ' ( ')).replace(')', ' ) ')).split() if x.strip() != '']


global toprocess
global topidx

toprocess=""
topidx=0

def decisiontree(): #uses lefttoprocess and topidx!
	global topidx
	if toprocess[topidx] != '(':
		raise ValueError
	topidx+=1
	ans=[float(toprocess[topidx])]
	topidx+=1
	if toprocess[topidx] == ')':
		topidx+=1
		return ans
	ans.append(toprocess[topidx])
	topidx+=1
	ans.append(decisiontree())
	ans.append(decisiontree())
	if toprocess[topidx] != ')':
		raise ValueError
	topidx+=1
	return ans


def prob(tree, attrib):
	if len(tree) == 1:
		return tree[0]
	if tree[1] in attrib:
		return tree[0]*prob(tree[2], attrib)
	else:
		return tree[0]*prob(tree[3], attrib)

import sys

rdln = sys.stdin.readline

N = int(rdln())

for case in range(1, N+1):
	L = int(rdln())
	inp = ""
	for i in range(L):
		inp+=" "
		inp+=rdln()
	global toprocess
	toprocess=tokenize(inp)
	global topidx
	topidx=0
	tree = decisiontree()
	
	print("Case #", case, ":", sep="")
	A = int(rdln())
	for i in range(A):
		print("{0:.9f}".format(prob(tree, set([x.strip() for x in rdln().split() if x.strip() != ''][2:]))))
