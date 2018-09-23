





def solve(L):
	numhorses = int(L[0][1])
	horselist = L[1:]
	dest = int(L[0][0])

	mintime = (dest - int(horselist[0][0]))/float(int(horselist[0][1]))


	for x in range(1,len(horselist)):
		currents = (dest - int(horselist[x][0]))/float(int(horselist[x][1]))
		if (currents > mintime):
			mintime = currents
		else:
			continue

	return dest/mintime







file = open("input1.txt")
L = file.read().splitlines()

num = int(L[0])
inp = []
count = 0
for x in range(1,len(L)):
	n = L[x].split(" ")	

	inp.append(n)

new = True
index = 0
kk = []

while(index < len(inp)):
	if(new):
		k = []
		count = int(inp[index][1])
		
		for x in range(count+1):
			k.append(inp[index + x])
		kk.append(k)
		index = index + count + 1




for x in range(0,num):
	ans = solve(kk[x])
	print ("Case #{}: {}".format(x+1, ans))






