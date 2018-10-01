import sys
sys.setrecursionlimit(100000)
def calculate_time(farm,rate,f,target,elapsed):
	if ( target/rate > farm/(rate) + target/(rate + f)):
		return calculate_time(farm,rate + f, f,target, elapsed + farm/rate)
	else:
		return target/rate + elapsed

input_file = open('B-small-attempt1.in','r')
input_text = input_file.read()
output = ""
output_file = open('B_output_small_attempt0','w')
i = 0
for line in input_text.split('\n'):
	if (i == 0):
		i = i +  1
		num_of_tests = line
		continue
	params = line.split(' ')
	if (params[0] == ''):
		continue

	print (params)
	time = calculate_time(float(params[0]),2.0,float(params[1]),float(params[2]),0.0)
	
	output += 'Case #' + str(i) + ': ' + str(time) + '\n'

	i+=1

print (output)

output_file.write(output)