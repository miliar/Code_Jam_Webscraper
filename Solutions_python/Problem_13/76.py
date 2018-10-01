def left(idx): return (idx + 1) * 2 -1
def right(idx): return (idx + 1) * 2

def change(nodes, idx):
	if nodes[idx]["b"] == 1:
		nodes[idx]["b"] = 0
	else:
		nodes[idx]["b"] = 1

def changeAsSelection(nodes, changables, selection):
	for j, c in enumerate(selection):
		if c == 1 :
			change(nodes, changables[j])

def doSolve(nodes, changables, target):
	if evaluateNode(0, nodes) == target: return 0
	for i in range(1, len(changables)+1):
		seed = buildSeed(len(changables), i)
		while(True):	
			changeAsSelection(nodes, changables, seed)
			if evaluateNode(0, nodes) == target:
				return i
			changeAsSelection(nodes, changables, seed)
			if not enumerateCombination(seed): break
	return -1

def buildSeed(total, select):
	if total < select: return []
	result = []
	for i in range(1, select+1) : result.append(1)
	for i in range(select+1, total+1) : result.append(0)
	return result

def enumerateCombination(arr, tail=-1):
	if tail == -1 : tail = len(arr) - 1
	if tail == 0 : return False
	lastOneIdx = findLastOneIdx(arr, tail)
	if lastOneIdx < 0 : return False
	arr[lastOneIdx] = 0
	if lastOneIdx == tail:
		if not enumerateCombination(arr, tail - 1) : return False
		lastOneIdx = findLastOneIdx(arr, tail-1)
	arr[lastOneIdx+1] = 1
	return True

def findLastOneIdx(arr, tail=-1):
	if tail == -1 : tail = len(arr) - 1
	for i in range(tail, -1, -1):
		if arr[i] == 1:
			return i
	return -1

def evaluateNode(idx, nodes):
	if nodes[idx]["i"]:
		a = evaluateNode(left(idx), nodes)
		b = evaluateNode(right(idx), nodes)
		if nodes[idx]["b"] == 1:
			return a and b
		else:
			return a or b
	else:
		return nodes[idx]["v"]

def main():
	import sys
	for i in range(1, int(sys.stdin.readline())+1):
		meta=map(lambda a:int(a), sys.stdin.readline().split())
		V=meta[1]
		nodes=[]
		changables=[]
		interiors = (meta[0]-1)/2
		for j in range(meta[0]):
			if j < interiors:
				n= map(lambda a:int(a), sys.stdin.readline().split())
				nodes.append({"i":True, "b":n[0], "c":n[1]})
				if n[1] == 1: changables.append(j)
			else:
				n= int(sys.stdin.readline())
				nodes.append({"i":False, "b":-1, "v":n})
		res = doSolve(nodes, changables, V)
		if res < 0: res = "IMPOSSIBLE"
		print "Case #" + str(i) + ": "+ str(res)

if __name__ == "__main__" : main()
