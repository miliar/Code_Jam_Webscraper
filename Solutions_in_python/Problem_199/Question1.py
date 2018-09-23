



def stringtoList(s):
	L = []
	for i in range(len(s)):
		if(s[i] == "+"):
			L.append(True)
		else:
			L.append(False)
	return L

def calc(L,s):
	k = L
	kk = [0]
	def solve(i):
		if(s+i > len(k)):
			for n in range (i, len(k)):
				if(k[n] == False): 
					kk[0] = -1
			return 
		else:
			if(k[i] == False):
				kk[0] += 1
				for x in range(0,s):
					k[x+i] = not k[i+x]
				return solve(i+1)
			else:
				return solve(i+1)
	solve(0)
	return kk[0]

def callWithLargeStack(f,*args):
    import sys
    import threading
    threading.stack_size(2**27)  # 64MB stack
    sys.setrecursionlimit(2**27) # will hit 64MB stack limit first
    # need new thread to get the redefined stack size
    def wrappedFn(resultWrapper): resultWrapper[0] = f(*args)
    resultWrapper = [None]
    #thread = threading.Thread(target=f, args=args)
    thread = threading.Thread(target=wrappedFn, args=[resultWrapper])
    thread.start()
    thread.join()
    return resultWrapper[0]

file = open("input1.txt")
L = file.read().splitlines()

k = L[0]
for x in range(1,int(k)+1):
	r = L[x].split(" ")
	ans = callWithLargeStack(calc,stringtoList(r[0]),int(r[1]))
	print ("Case #{}: {}".format(x, ans if ans != -1 else "IMPOSSIBLE"))



