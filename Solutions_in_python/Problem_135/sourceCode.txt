t = int(raw_input())
k = 1
num = 0
while t>0:
	r1 = int(raw_input())
	list1 = []
	list1.append(raw_input().split())
	list1.append(raw_input().split())
	list1.append(raw_input().split())
	list1.append(raw_input().split())
 
	r2 = int(raw_input())
	list2 = []
	list2.append(raw_input().split())
	list2.append(raw_input().split())
	list2.append(raw_input().split())
	list2.append(raw_input().split())
 
	selected1 = list1[r1-1]
	selected2 = list2[r2-1]
	count = 0
	l = str(k)
	for i in selected1:
		if i in selected2:
			count += 1
			num = i;
	if count == 1:
		ans = str(num)
	elif count > 1:
		ans = "Bad magician!"
	elif count == 0:
		ans = "Volunteer cheated!"
 
	print "Case #" + l + ": " + str(ans)
 
	k += 1
	t -= 1