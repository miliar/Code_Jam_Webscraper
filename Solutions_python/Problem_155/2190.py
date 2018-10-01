if __name__ == '__main__':
	T= int(raw_input().strip())
	for t in xrange(T):
		[Smax,X]= map(str,raw_input().strip().split())
		X=map(int,X)
		
		agrego = 0
		if(Smax != 0):
			suma = X[0]			
			for i in xrange(1,len(X)):
				if X[i]>0 and suma+agrego < i:
					agrego += (i-suma-agrego)					
				suma += X[i]

		print "Case #"+str(t+1)+':', agrego