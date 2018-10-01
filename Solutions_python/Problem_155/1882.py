f = open('input.txt', 'r')
o = open('output.txt', 'w')
case = int(f.readline())

for x in range(case):
	arr1 = f.readline()
	arr1 = arr1.split(" ")
	arr1 = arr1[len(arr1)-1][:len(arr1[len(arr1)- 1])-1]
	s = []

	for a in arr1:
		s.append(int(a))
	su = 0
	friends = 0
	count1 = 0
	while count1 < len(s):
		if su < count1 and s[count1] > 0:
			friends += (count1) - su
			su += (count1)
		su += s[count1]
		count1 += 1
	o.write("Case #" + str(x+1) + ": " + str(friends) + "\n") 
