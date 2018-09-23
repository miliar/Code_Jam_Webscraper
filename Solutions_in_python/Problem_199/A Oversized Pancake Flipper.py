

def flip(pancake_str, flipper_size):
	"""
	Input : string that is sequence of face sign of pancake, and size of flipper
	Output : minum number of flip or impossible.
	"""
	if len(pancake_str)<flipper_size:
		return 'IMPOSSIBLE'
	pancake=[]
	for item in pancake_str:
		pancake.append(item)


	count=0
	for item in range(len(pancake)-1,flipper_size-2,-1):
		if pancake[item]=='-':
			count+=1
			for item2 in range(item,item - flipper_size,-1):
				if pancake[item2]=='+':
					pancake[item2]='-'
				else:
					pancake[item2]='+'
			#print pancake
	for item in range(flipper_size-1):
		#print item,pancake[item]
		if pancake[item]=='-':
			return 'IMPOSSIBLE'
	return count





# print flip('---+-++-', 3)
# print flip('+++++', 4)
# print flip('-+-+-', 4)
def test_case(number):
	test=''
	for item in range(number):
		if item%2==0:
			test+='+'
		else:
			test+='-'
	return test
# a=test_case(1000)
# print a, len(a)

# print flip(a,5)
# print flip(a,127)


f_out = open('A_output_large.txt', 'w')
f_in = open('A-large.in', 'r')
#print f_in.readlines()
lines = [line.strip() for line in f_in.readlines()][1:]
#test_case=[]
#one_case=[]

#lines=['---+-++- 3','+++++ 4', '-+-+- 4']

print lines

for idx in range(len(lines)):
	pancake,flipper=lines[idx].split()
	flipper=int(flipper)
	ans = flip(pancake,flipper) 
		
	# writes an answer (in a new line) to the output file
	f_out.write("Case #{0}: {1}\n".format(idx+1, ans))

f_out.close()
