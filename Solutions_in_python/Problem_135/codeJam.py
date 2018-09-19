def compareLines(arr1, arr2):
	intersection = set(arr1) & set(arr2)
	if(len(intersection) > 1):
		return "Bad magician!"
	if(len(intersection) == 1):
		return str(list(intersection)[0])
	else:
		return "Volunteer cheated!"
	

f = open('A-small-attempt0.in', 'r')

cases = int(f.readline())

firstlist = []
secondlist = []

for j in range(0, cases):
	targetrow = int(f.readline())
	for i in range(1, targetrow):
		f.readline()
	firstlist = f.readline().split()
	for i in range(targetrow, 4):
		f.readline()
	targetrow = int(f.readline())
	for i in range(1, targetrow):
		f.readline()
	secondlist = f.readline().split()
	for i in range(targetrow, 4):
		f.readline()
	print "Case #" + str(j+1) + ": " + compareLines(firstlist, secondlist)

