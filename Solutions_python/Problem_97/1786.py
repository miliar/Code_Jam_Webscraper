out = open("C:\Users\Andrew\Desktop\output.txt", "w")
openfile = open('C:\Users\Andrew\Desktop\C-small-attempt1.in', 'r')
inputs = openfile.readlines()
case = 1
inputs.pop(0)
for x in range(0, len(inputs)):
	inputs2 = inputs.pop(0)
	A, B = (map(int, inputs2.split()))
	list1 = []
	list2 = []

	for x in range(A, B+1):
		for y in range(A, B+1):
			if y > x:
				for z in range(0,len(str(x))):
					v = int(str(x)[z:] + str(x)[0:z])
					if v == y:
						list1.append(v)
						list2.append((x,y))
	list1.sort()
	d = 0
	for x in list2:
		for y in list2:
			if x == y:
				d = d+1
			if d > 1:
				list2.remove(y)
				d = 0
		d = 0
	if case != 50:
		out.write("Case #%d: %d\n" % (case, len(list2))) 
	if case == 50:	
		out.write("Case #%d: %d" % (case, len(list2))) 
	case += 1
out.close()