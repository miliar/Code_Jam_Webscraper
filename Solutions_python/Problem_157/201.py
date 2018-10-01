#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import *
#from sets import *
import math
import sys

class Quaternion:
	element = '1'
	sign = 1
	def __init__(self, e, s=1):
		self.element = e
		self.sign = s
	def __str__(self):
		return str((self.sign, self.element))
	def __mul__(self, mul):
		a = self.element
		b = mul.element
		if a=='1':
			if b=='1':
				return Quaternion('1', 1*self.sign*mul.sign)
			elif b=='i':
				return Quaternion('i', 1*self.sign*mul.sign)
			elif b=='j':
				return Quaternion('j', 1*self.sign*mul.sign)
			elif b=='k':
				return Quaternion('k', 1*self.sign*mul.sign)
		elif a=='i':
			if b=='1':
				return Quaternion('i', 1*self.sign*mul.sign)
			elif b=='i':
				return Quaternion('1', -1*self.sign*mul.sign)
			elif b=='j':
				return Quaternion('k', 1*self.sign*mul.sign)
			elif b=='k':
				return Quaternion('j', -1*self.sign*mul.sign)
		elif a=='j':
			if b=='1':
				return Quaternion('j', 1*self.sign*mul.sign)
			elif b=='i':
				return Quaternion('k', -1*self.sign*mul.sign)
			elif b=='j':
				return Quaternion('1', -1*self.sign*mul.sign)
			elif b=='k':
				return Quaternion('i', 1*self.sign*mul.sign)
		elif a=='k':
			if b=='1':
				return Quaternion('k', 1*self.sign*mul.sign)
			elif b=='i':
				return Quaternion('j', 1*self.sign*mul.sign)
			elif b=='j':
				return Quaternion('i', -1*self.sign*mul.sign)
			elif b=='k':
				return Quaternion('1', -1*self.sign*mul.sign)
		raise ValueError('multiplication error, %s, %s', str(self), self(mul))
	def __eq__(self, c):
		return self.sign == c.sign and self.element == c.element

def linear_search(line, target, begin, end):
	l = len(line)
	mul = Quaternion('1')
	for i in range(begin, end):
		mul = mul * Quaternion(line[i%l])
		if mul == target:
			return i
	return end


if __name__ == "__main__":
	t = int(input())
	for caseIdx in range(1,t+1):
		sys.stdout.flush()
		l, x = map(int, input().split(' '))
		line = input()

		begin = 0
		end = min(l*x,begin+l*4)
		# find first i
		ret = linear_search(line, Quaternion('i'), begin, end)
		if ret==end:
			print("Case #%d: %s" % (caseIdx, "NO"))
			continue

		begin = ret+1
		end = min(l*x,begin+l*4)
		# find first j
		ret = linear_search(line, Quaternion('j'), begin, end)
		if ret==end:
			print("Case #%d: %s" % (caseIdx, "NO"))
			continue

		begin = ret+1
		end = min(l*x,begin+l*4)
		# find first k
		ret = linear_search(line, Quaternion('k'), begin, end)
		if ret == end and ret != l*x:
			print("Case #%d: %s" % (caseIdx, "NO"))
			continue

		begin = ret+1
		end = (l*x - begin)%(l*4)+begin
		mul = Quaternion('1')
		for i in range(begin, end):
			mul = mul * Quaternion(line[i%l])
		if mul == Quaternion('1'):
			print("Case #%d: %s" % (caseIdx, "YES"))
		else:
			print("Case #%d: %s" % (caseIdx, "NO"))
