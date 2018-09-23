def main():
	
	f = open("C-small-1-attempt0.in", "r")
	lines = f.readlines()
	f.close()
	w = open("output.txt", "w")
	n = lines[0]

	for i in range(int(n)):
		l = i + 1
		n,k = lines[l].split(" ")
		n = int(n)
		k = int(k)
		w.write("Case #"+str(l)+": "+solve(n,k)+'\n')

	w.close()

def solve(n, k):
	#initial listL and listR
	listL = list(range(n))
	listR = list(range(n))
	listR.reverse()	
	listMinLR = [0] * n
	listMaxLR = [0] * n
	result = ""
	while(k>0):	
		for i in range(n):
			listMinLR[i] = min(listL[i],listR[i])
			listMaxLR[i] = max(listL[i],listR[i])

		minLR = max(listMinLR)
		counts = listMinLR.count(minLR)
		maxLR = -1
		index = -1
		if(counts == 1):
			index = listMinLR.index(minLR)
			maxLR = listMaxLR[index]
		else:
			for j in range(n):
				if(listMinLR[j] == minLR):
					if(listMaxLR[j] > maxLR):
						index = j
						maxLR = listMaxLR[j]


		updateLR(listL,listR,index,n)

		k=k-1
		if(k==0): result = str(maxLR) + " " + str(minLR)
	return result
def updateLR(listL, listR, index,n):
	for i in range(n):
		if(i == index):
			listL[i] = -1
			listR[i] = -1
		elif(i < index):
			if(listR[i] != -1):
				listR[i] = min(listR[i], index - i -1)
		else:
			if(listL[i] != -1):
				listL[i] = min(listL[i], i - index - 1)
	# print("listL: " + str(listL))
	# print("listR:",listR)

if __name__ == '__main__':
	main()