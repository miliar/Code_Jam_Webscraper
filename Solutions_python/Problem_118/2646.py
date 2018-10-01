import math
palins=set()
squares=set()
notpalins=set()
notsquares=set()
def isPalin(num):
	if num in palins:
		return True
	if num in notpalins:
		return False
	x=str(num)
	if len(x)==1:
		palins.add(num)
		return True
	for k in range(len(x)/2):
		if x[k]!=x[len(x)-k-1]:
			notpalins.add(num)
			return False
	palins.add(num)
	return True
def isSquare(num):
	if num in squares:
		return True
	if num in notsquares:
		return False
	issquare=math.sqrt(num)==int(math.sqrt(num)) and isPalin(int(math.sqrt(num)) )
	if issquare:
		squares.add(num)
	else:
		notsquares.add(num)
	return issquare

inp=open('input2.txt').read().rsplit('\n')
count=int(inp[0])
for cs in range(1, count+1):
	print "Case #%d: "%cs,
	arr=inp[cs].rsplit()
	start=int(arr[0])
	end=int(arr[1])
	k=0
	for tr in range(start, end+1):
		if isSquare(tr) and isPalin(tr):
			k+=1
	print k