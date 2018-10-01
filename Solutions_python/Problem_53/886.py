#tyloslinger at work...yeah babe....ha haaaa lol.....

f = open("A-large.in","r")
w = open("tylos2_out.txt","w")
N = int(f.readline())
for i in range(1, N+1):
	S = map(int, f.readline().split())
	n = S[0]
	k = S[1]
	r = "OFF"
	
	if n > k or n == k and k != 1: pass
	elif n == k and k == 1: r = "ON"		
	else:
		k0 = 2**n - 1
		if k0 > k: r = "OFF"
		elif k0 == k: r = "ON"
		else:
			d = 2**n
			v = k % d
			if d == (v + 1): r = "ON"
			else: r = "OFF"
	w.write("Case #{0}: {1}\n".format(i, r))
f.close()
w.close()