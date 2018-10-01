def stalls(n, k):

	bits = k.bit_length()-1
	numpairs = 2**bits
	num = 2*numpairs

	if num>n: return (0,0)
	mini = (n-num+1)//num
	mod = (n-num+1)%num

	ls = mini
	rs = mini
	# print("\t",num,numpairs,mini)

	pos = k - numpairs
	if mod>numpairs:
		rs+=1
		mod-=numpairs
		# increase left depending on value of k
		if mod>pos:
			ls+=1
	elif mod>pos:
		# increase right depending on value of k
		rs+=1

	return (rs, ls)

inf = open("C-large.in","r")
outf = open("output.txt","w+")
num = int(inf.readline())
for c in range(num):
	dat = inf.readline().split()
	n = int(dat[0])
	k = int(dat[1])
	res = stalls(n,k)
	outf.write('Case #%d: %d %d\n'%((c+1),res[0],res[1]))

inf.close()
outf.close()
