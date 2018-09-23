reader = open("B-large.in")
writer = open("B-large.out", "w") #writer.write(string + "\n")

def update(value):
	#print(value)
	m = value[0:1]
	for i in range(1,len(value)):
		num = value[i:i+1]
		#print(str(i)+" "+num+" "+m)
		if(num<m):
			#value[i-1:i] = str(int(value[i-1:i])-1)
			#print("Pre "+value)
			value = value[0:i-1] + str(int(value[i-1:i])-1) + value[i:len(value)]
			#print("Cur "+value)
			for r in range(i+1,len(value)+1):
				value = value[0:r-1] + "9" + value[r:len(value)]
			if(value[0:1]=="0"):
				value = value[1:len(value)]
			#print("Post "+value)
			return value, False
		else:
			#print("Else "+value)
			m = num
	#print("Clear: "+str(len(value))+" "+value)
	return value, True

N = int(reader.readline())
print(N)
for itr in range(0,N):
	current = reader.readline()
	if(itr<N):
		current = current[0:len(current)-1]
	print("Case #"+str(itr+1)+": "+current)
	#ctr = 0
	res = update(current)
	#while(res[1] == False and ctr<5):
	while(res[1] == False):
		res = update(res[0])
		#ctr+=1
	print("Case #"+str(itr+1)+": "+res[0])
	writer.write("Case #"+str(itr+1)+": "+res[0]+"\n")