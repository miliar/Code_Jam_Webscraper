#!/usr/bin/python
import sys

data = sys.stdin.readlines()
cases = int(data.pop(0))
case = 1

while (case <= cases):
	sys.stdout.write("Case #%d: [" % case)
	line = data.pop(0) #get the line
	words = line.split() #separate by spaces
	combine = {}
	C = int(words.pop(0)) #no. of combines
	i = 0
	while i < C: #create combines dictionary
		temp = words.pop(0)
		key1 = temp[0:2]
		key2 = key1[::-1] #reverse of key1
		val = temp[2]
		combine[key1] = val
		combine[key2] = val
		i += 1
	
	opposed = {} #opposed dictionary
	D = int(words.pop(0))
	i = 0
	while i < D:
		temp = words.pop(0)
		index = 0
		# create or add to dictionary of lists (twice for mirror image)
		# e.g. opposed['a'] = [ b, c, d]
		# and  opposed['c'] = [ a ]
		while index < 2:
			if opposed.has_key(temp[index]):
				opposed[temp[index]].append(temp[index-1])
			else:
				opposed[temp[index]] = [ temp[index-1] ]
			index += 1
		i += 1
		
	N = int(words.pop(0))
	invoke = list(words.pop(0))
	invokeList = []
	for element in invoke:
		invokeList.append(element)
		if len(invokeList) > 1:
			#check for combining
			AB = invokeList[-2] + invokeList[-1] #last 2 elements in invokeList as string
			if combine.has_key(AB):
				invokeList.pop(-1)
				invokeList.pop(-1) # remove last 2 element from invoke list
				invokeList.append(combine[AB]) #add it's combination
			else: #didn't combine
				if opposed.has_key(element): #it has oppositions defined
					for character in invokeList[:-1]: #check each character (except last) of invokeList
						if character in opposed[element]:
							del invokeList[:]
	
	output = ''
	for element in invokeList:
		output = output + element + ', '
	
	output = output[:-2] #trim last ', '
	sys.stdout.write(output + "]\n")
	case += 1