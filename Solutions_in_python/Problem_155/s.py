index = 1
for i in range(input()):
	s,arr = map(str,raw_input().split())
	s = int(s)
	arr = map(int,str(arr))
	if s==0: ans = 0
	else:
		add = 0
		standing_till_now = arr[0]
		for shy_level in range(1,s+1):
			if arr[shy_level]>0:
				if standing_till_now>=shy_level:
					standing_till_now += arr[shy_level]
				else:
					add += shy_level - standing_till_now
					standing_till_now += arr[shy_level] + add
		ans = add
	print "Case #"+str(index)+": "+str(ans)
	index += 1
