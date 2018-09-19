def ugly(number):
	if number == 0:
		return 1
	for x in [2, 3, 5, 7]:
		if number % x == 0:
			return 1
	return 0
	
def permute2(part_sols, rest):
	retval = []
	if len(rest) == 0:
		return [ {"sum" : x["sum"] + eval(x["x"]), 
		    "x" : ""} for x in part_sols]
	for part_sol in part_sols:
		retval += permute2(
		          [{'sum' : part_sol['sum'], 
		            "x"  : part_sol["x"]    + rest[0]}], rest[1:])
		retval += permute2(
		          [{'sum' : part_sol['sum'] + eval(part_sol["x"]), 
		            "x"  : "+" + rest[0]}], rest[1:])
		retval += permute2(
		          [{'sum' : part_sol['sum'] + eval(part_sol["x"]), 
		             "x"  : "-" + rest[0]}], rest[1:])
	return retval
		
	
def permute(stream):
	retval = []
	for i in xrange(len(stream)):
		base = int(stream[0:i+1])
		if i + 1 == len(stream):
			retval.append(base)
			continue
		for ptation in permute(stream[i + 1:]):
			for x in (base + ptation, base - ptation):
				retval.append(x)
	return retval
	
#lala = 1
lala = int(raw_input())
import time
for count in xrange(lala):
	combinations = []
	stream = raw_input()
	#stream = "110"
	result = reduce(lambda x, y: ugly(y) + x, permute(stream), 0)
	#result2 = reduce(lambda x, y: ugly(y["sum"]) + x,
  	#	permute2([{"sum" : 0, "x" : stream[0]}], stream[1:]), 0)
	#print stream, combinations, 3 ** (len(stream) - 1), len(combinations)
	print "Case #%s: %s" % (count + 1, result)
