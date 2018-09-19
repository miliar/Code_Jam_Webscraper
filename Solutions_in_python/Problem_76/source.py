#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def doit():
	input = open("C.in", 'r')
	output = open("C.out", 'w')
	T = int( input.readline() )
	
	i = 0
	while i < T:
		N = int( input.readline() )
		line = input.readline().split()
		values = []
		
		for j in line:
			values.append( int(j) )
		
		#print values
		out = compute( values )
		
		output.write( "Case #"+str(i+1)+": "+out+"\n" )
		
		i = i+1
	
	output.close()
	input.close()


def compute( values ):
	out = 0
	
	values.sort()
	patrick = values.pop(0)
	
	for i in values:
		patrick = patrick ^ i
		out = out + i
	
	if patrick != 0:
		return "NO"
	
	return str(out)


doit()
