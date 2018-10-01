T=int(raw_input())
for t in xrange(T):
	N=int(raw_input())
	w=[]
	for n in xrange(N):
		w+=[raw_input()]
	wint=[]
	lint=[]
	for n in xrange(N):
		wint+=[w[n].count("1")]
		lint+=[w[n].count("0")]
	wp=[]
	for n in xrange(N):
		wp+=[wint[n]*1./(wint[n]+lint[n])]
	owp=[]
	for n in xrange(N):
		count=0
		sum=0
		for i in xrange(N):
			if w[n][i]!=".":
				count+=1
				wj=0
				lj=0
				for j in xrange(N):
					if j!=n:
						if w[i][j]=="1": wj+=1
						if w[i][j]=="0": lj+=1
				sum+=wj*1./(wj+lj)
		owp+=[sum/count]
	oowp=[]
	for n in xrange(N):
		count=0
		sum=0
		for i in xrange(N):
			if w[n][i]!=".":
				count+=1
				sum+=owp[i]
		oowp+=[sum/count]
	rpi=[]
	for n in xrange(N):
		rpi+=[0.25*wp[n]+0.5*owp[n]+0.25*oowp[n]]
	print "Case #%d: " %(t+1)
	for n in xrange(N):
		print rpi[n]