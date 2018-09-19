import os

def read_vector(s):
	return [i for i in s.split(" ")]

filepath = "/home/mike/Downloads/"
filename = "B-small-attempt2"

f_in = open(os.path.join(filepath, filename+".in"), "rb")
f_out = open(os.path.join(filepath, filename+".out"), "wb")
num_test_cases = int(f_in.readline())

for test_case in xrange(1, num_test_cases+1):
	combine = {}
	oppose = {}
	
	V = read_vector(f_in.readline())
	
	C = int(V.pop(0))
	for i in xrange(0, C):
		s = V.pop(0)
		combine[s[0:2]] = combine[s[1::-1]] = s[2]

	D = int(V.pop(0))
	for i in xrange(0, D):
		s = V.pop(0)
		oppose[s[0]] = s[1]
		oppose[s[1]] = s[0]

	N = int(V.pop(0))
	char = V.pop(0)
	
	#print "combine:", combine
	#print "oppose:", oppose
	#print N, char
				
	element_list = []
	for i in xrange(0, N):
		try:
			new_element = combine[char[i]+element_list[-1]]
			element_list.pop()
			element_list.append(new_element)
		except:
			try:
				oppose_element = oppose[char[i]]
			except:
				oppose_element = None
				
			if (element_list.count(oppose_element)): 
				element_list = []
			else:
				element_list.append(char[i])

			
	#print element_list
	#print
	
	output = "Case #%d: %s" % (test_case, element_list)
	output = output.replace("'", "")
	print output
	f_out.write(output+"\n")

f_out.close() 