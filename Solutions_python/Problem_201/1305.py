from math import *

def mergePatch(patch, patches):
	i = 0
	while i < len(patches) and patch[0] < patches[i][0]:
		i += 1
	
	if i < len(patches) and patch[0] == patches[i][0]:
		patches[i] = patch[0], patch[1] + patches[i][1]
	else:
		patches.insert(i, patch)


def testCase(N, K, i):
	patches = [(N, 1)]
	
	while True:
		patch = patches.pop(0)
		K -= patch[1]
		low = floor((patch[0]-1)/2.0)
		hgh = ceil((patch[0]-1)/2.0)
		mergePatch((low, patch[1]), patches)
		mergePatch((hgh, patch[1]), patches)
		#print(patches)
		if K <= 0:
			print("Case #" + str(i+1) + ": " + str(hgh) + " " + str(low))
			return
		


T = int(input())

for i in range(0, T):
	line = input()
	N = int(line.split(" ")[0])
	K = int(line.split(" ")[1])
	
	#print(N)
	#print(K)
	
	testCase(N, K, i)
		
		#if N <= 0:
		#	a = 
		

