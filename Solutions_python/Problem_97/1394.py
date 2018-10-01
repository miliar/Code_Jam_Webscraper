import io
 
def rotate(letters, n):
	return letters[n:] + letters[:n]
 
def algorithm3(data):
	#data = trim($data[0]);
	data = data.split(' ')
	#print data
	
	if len(data)<2:
		return 0
		
	A =  (int(data[0]))
	B =  (int(data[1]))
	
	current_n = None
	current_m = None

	# 1 digit, no solution:
	if (len(str(A)) == 1 and len(str(B)) == 1):
		return 0

 
	result = {}
	ranges = range(int(A),int(B)) 
	count = 0
	
	#print ranges
	
	for i,elem in enumerate(ranges):
		
		current_n = int(ranges[i])*1
		current_m = int(ranges[i])*1
		length = len(str(ranges[i]))

		for j in range(0,length):
			# rotate string to get m value:
			#current_m = (int)substr(current_m, -1) . substr($current_m, 0, $length - 1);
			#print current_n			print current_m 
			#print current_n 		, ' ', 	current_m 	, " -> "	,
			current_m =  rotate(str(current_m),1)
						
			#print current_m
			
			#print A , ' ', B 
			#print int(str(current_n) + str(current_m))
			# A = n < m = B
			#print int(current_m) <= B
			if (int(current_m) <= B and int(current_m) > int(current_n) and int(current_m) >= A ):        
			  result[int(str(current_n) + str(current_m))] = True
			  #echo "($current_n, $current_m) . count: " . count($result) . " \n";
			  #print "Ok (", current_n , " ",  current_m , ") . count: " , len(result) ,# int(str(current_n) + str(current_m)), "\n"

	#print result
	return len(result) 
		
"""
print algorithm3('4')
print algorithm3('10 40')
print algorithm3('100 500')
print algorithm3('1111 2222')
"""

rowC = 0

o = open('output_large.txt','w')	
i = open('C-large.in','r')

for index, line in enumerate(i.readlines()):
	
	if (index==0):
		max = i.readlines()
	if (index>0 and index <max):
		o.write('Case #' + str(rowC) + ': ' + str(algorithm3(line)) + '\r\n' )		
	rowC+=1
	
i.close()
o.close()

