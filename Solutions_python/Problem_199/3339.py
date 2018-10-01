def flip(state,start,flipSize):
	res=""
	res=res+state[:start]
	for i in range (start,start+flipSize):
		if state[i]=="+":
			res=res+"-"
		else:
			res=res+"+"
	res=res+state[start+flipSize:]
	return res
def solved(state):
	try:
		state.index("-")
	except ValueError:
		return True
	else:
		return False
def solve(state,flipSize):
	lenState=len(state)
	res=0
	while not solved(state):
		minusCount=0
		for i in range(lenState):	
			if state[i]=="-":
				minusCount+=1
			elif state[i]=="+":
				minusCount=0
			if minusCount==flipSize:
				state=flip(state,i-flipSize+1,flipSize)
				res+=1
				minusCount=0
		flipped=False
		for i in range(lenState-flipSize):
			if state[i]=="-":
				state=flip(state,i,flipSize)
				res+=1
				flipped=True
				break
		if not flipped:
			flag2=solved(state)
			if flag2:
				return res
			else:
				return -1
		if res>10000:
			return -1
	return res

tasklist=[]
lines = [line.rstrip('\n') for line in open('q1.inp')]
taskcount=int(lines.pop(0));
for i in range(taskcount):
	state,flipSize=lines.pop(0).split(" ")
	flipSize=int(flipSize)
	res=solve(state,flipSize)
	if res!=-1:
		print ("Case #"+str(i+1)+":"),res
	else:
		print("Case #"+str(i+1)+": IMPOSSIBLE")
		
	
	
