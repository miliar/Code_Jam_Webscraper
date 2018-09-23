import numpy as n
theData = n.loadtxt("data.in",skiprows = 1)
rows=theData.shape[0]
i=0
def cutleft(N):
	if N %2 ==0:
		return N/2 -1 
	else:
		return (N-1)/2
def cutright(N):
	if N %2 ==0:
		return N/2
	else:
		return (N-1)/2

while i<rows:
	j=0
	N = theData[i][0]
	thecuts = []
	thecuts.append(cutleft(N))
	thecuts.append(cutright(N))
	while j<theData[i][1] -1:
		thecuts.append(cutleft(max(thecuts)))
		thecuts.append(cutright(max(thecuts)))
		j+=1
		thecuts.remove(max(thecuts))
	print()
	print("Case #"+str(i+1)+":",int(thecuts[-1]),int(thecuts[-2]))
	i+=1