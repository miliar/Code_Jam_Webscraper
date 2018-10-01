
memory = {
	1: [0, 1],
	2: [1, 1],
	3: [1, 2],
	4: [2, 2],
	5: [2, 3],
	6: [3, 3],
	7: [3, 4],
	8: [4, 4],
	9: [4, 5]
}

t = int(input())
cnt = 1

while (t):
	x = int(input())

	li = list(input().split())
	li = [int(i) for i in li]
	liUnMod = [int(i) for i in li]

	arr9 = [float("inf")]
	index = 0
		
	# print(liUnMod)

	if li.count(9) is 1:
		while any(i>1 for i in li):
			maxEle = max(li)
	
			arr9.append(maxEle+ index)
			index += 1
			
			if maxEle is 9:
				li.append(3)
				li.append(6)
			else:
				li.append(memory[maxEle][0])
				li.append(memory[maxEle][1])
			
			i = li.index(maxEle)
			del(li[i])
		# print("Case #"+ str(cnt) + ": " + str(min(arr9)))

	li = liUnMod
	arr = [float("inf")]
	index = 0
	# print(li)

	if any(i>1 for i in li):
		while any(i>1 for i in li):
			maxEle = max(li)
	
			arr.append(maxEle+ index)
			index += 1
			
			li.append(memory[maxEle][0])
			li.append(memory[maxEle][1])
			
			i = li.index(maxEle)
			del(li[i])

		print("Case #"+ str(cnt) + ": " + str(min(min(arr), min(arr9))))
			
	else:		
		print("Case #"+ str(cnt) + ": 1")

	t -= 1
	cnt += 1