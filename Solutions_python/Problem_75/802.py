

def solve(string,last,oppose,combine,lenString):
	if(len(string) == 0):
		string.append(last)
		return string
	
	#if(lenString == 1):
	for com in combine:
		if com[0] == string[-1] and com[1] == last:
			string.pop()
			string.append(com[2])
			return string
			
	for op in oppose:
		for a in string:
			#print last,a
			if op[0] == a and last == op[1]:
				#print "opp found"
				return []
	string.append(last)
	return string



file = open("input.txt")
num = int(file.readline())
FINAL = ""
for i in range(num):
	array = file.readline().split()
	#print array
	
	#parse the arry
	combine = []
	oppose = []

	for x in range(int(array[0])):
		combine.append(array[x+1][0:3])
		combine.append(array[x+1][1]+array[x+1][0]+array[x+1][2])
	off = int(array[0])+1
	
	
	for y in range(int(array[off])):
		oppose.append(array[y+off+1][0:2])
		oppose.append(array[y+off+1][::-1])
	#print oppose

	off += int(array[off])+1
	length = int(array[off])
	string = []
	s = array[off+1]
	for cc in s:
		string.append(cc)
	if(len(string) != 1):
		solution = []
		solution = solve([string[0]],string[1],oppose,combine,len(string)-2)
		string = string[2:]
		while len(string) > 0:
			solution = solve(solution,string[0],oppose,combine,len(string))
			string.pop(0)
	else:
		solution = string
	#print str(solution)
	s = str(solution)
	temp = ''
	temp+= s[0]
	for l in range(len(solution)):
		temp+=s[l*5+2]
		temp += ', '
	temp = temp[0:-2]
	temp += s[-1]
	if len(temp) == 1:
		temp = "[]"
	print i+1
	FINAL += "Case #" + str(i+1) + ": " + temp + "\n"
	
fileO = open('out.txt',"w")
fileO.write(FINAL)
	
				
				
		
