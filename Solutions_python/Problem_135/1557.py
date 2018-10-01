T = int(raw_input())

def scanarr ():
	arr = []
	for i in range(4):
		lirt = raw_input().split()
		lirt = map(lambda x : int(x), lirt)
		arr.append(lirt)

	return arr

for i in range(T):
	row1 = int(raw_input()) - 1
	arr1 = scanarr()

	possibilities1 = set(arr1[row1])

	row2 = int(raw_input()) - 1
	arr2 = scanarr()

	possibilities2 = set(arr2[row2])

	# Set intersection Python style
	runway = possibilities1 & possibilities2

	if len(runway) == 0:
		print ("Case #%(id)s: Volunteer cheated!" % {"id" : i+1})

	if len(runway) > 1:
		print ("Case #%(id)s: Bad magician!" % {"id" : i+1})

	if len(runway) == 1:
		res = list(runway)[0]
		print ("Case #%(id)s: %(res)s" % {"id" : i+1, "res" : str(res)})