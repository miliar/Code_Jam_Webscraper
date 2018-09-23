def isHap(arr):
	for i in range(0,len(arr)):
		if arr[i] == '-':
			return False
	return True

def flip(subpan):
	return subpan.replace('+','t').replace('-','+').replace('t','-')

def firstInst(pans, flpr):
	for i in range(0,len(pans)-flpr+1):
		if pans[i] == '-':
			return i
	return "IMPOSSIBLE"


def optflip(pans, flpr):
	if isHap(pans):
		return 0
	n = firstInst(pans, flpr)
	if n == "IMPOSSIBLE":
		return "IMPOSSIBLE"
	else:
		temp = pans[n:n+flpr]
		temp = flip(temp)
		temp = list(temp)
		pans = list(pans)
		pans[n:n+flpr] = temp
		pans = pans[n:]
		pans = ''.join(pans)
		if optflip(pans, flpr) == "IMPOSSIBLE":
			return "IMPOSSIBLE"
		else:
			return optflip(pans, flpr) + 1

results=[]
with open('A-small-attempt0.in') as inputfile:
    for line in inputfile:
    	results.append(line.strip().split(','))

out = open("foo.txt", 'wb')
for i in range(1, int(results[0][0])+1):
	input = results[i][0].split()
	pans = input[0]
	flpr = int(input[1])
	out.write('Case #%s: %s \n' % (i, optflip(pans, flpr)))
