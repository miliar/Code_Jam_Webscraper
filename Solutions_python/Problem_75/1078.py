#!/usr/bin/env python

def main():
	inputf = open( "input", "r" )
	outputf = open( "output", "w" )
	data = inputf.read().split('\n')
	print data
        for idx, line in enumerate(data):
		if idx == 0: num = int(line)
		else:
			print '\n\nCase #'+str(idx)
			result = calculatecase( line )
			print result
			outputf.write('Case #'+str(idx)+': '+str(result)+'\n')

def calculatecase(data):
	combine = {}
	oppose = []
	nthdig = 0
	invoke = ""
	for bit in data.split(' '):
		if bit.isdigit():
			nthdig += 1
			continue
		elif nthdig == 1:
			combine[bit[0]+bit[1]] = bit[2]
			combine[bit[1]+bit[0]] = bit[2]
		elif nthdig == 2:
			oppose.append(bit)
		else: invoke = bit
	# Oppose bit
	start = None
	end = None
	i = 0
	dontinc = False
	while i < len(invoke):
		print invoke[i]+" "+invoke
		if i > 0:
			if invoke[i-1]+invoke[i] in combine:
				if start == i-1 or start == i: start = None
				invoke = invoke[:i-1]+combine[invoke[i-1]+invoke[i]]+invoke[i+1:]
				dontinc = True
				if i >= len(invoke): break
		for bit in oppose:
			if invoke[i] in bit:
				if start is None: start = i
				elif invoke[start] != invoke[i]: end = i
				if start is not None and end is not None:
					invoke = invoke[end+1:]
					dontinc = True
					i = 0
					start = None
					end = None
					continue
		if not dontinc:
			i += 1
		if dontinc:
			dontinc = False
	print invoke
	return str(list(invoke)).replace("'",'')

if __name__ == '__main__':
                main()
