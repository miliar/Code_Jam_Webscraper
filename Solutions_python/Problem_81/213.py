t=int(raw_input())
ca=0;
while t:
	t-=1;
	ca+=1;
	print 'Case #%d:'%ca
	n=int(raw_input())
	l=[]
	count=[]
	for i in range(0,n):
		l.append(raw_input())
	for i in range(0,n):
		zero=0;
		one=0;
		for j in range(0,n):
			if l[i][j]=='0':
				zero+=1
			if l[i][j]=='1':
				one+=1

		count.append([zero,one]);
#	print count
	for i in range(0,n):
		wp=float(count[i][1])/(count[i][0]+count[i][1]);
		owp=0.0;
		iowp=0.0;
		oowp=0.0;
		for j in range(0,n):
			if(i!=j and l[i][j]=='0'):
				owp+=float(count[j][1]-1)/(count[j][0]+count[j][1]-1);
			if(i!=j and l[i][j]=='1'):
				owp+=float(count[j][1])/(count[j][0]+count[j][1]-1);
		owp=owp/(count[i][0]+count[i][1]);
		for j in range(0,n):
			iowp=0.0
			if i!=j and l[i][j]!='.':
				for k in range(0,n):
					if(k!=j and l[k][j]=='0'):
						iowp+=float(count[k][1])/(count[k][0]+count[k][1]-1);
					if(k!=j and l[k][j]=='1'):
						iowp+=float(count[k][1]-1)/(count[k][0]+count[k][1]-1);
			iowp=iowp/(count[j][0]+count[j][1]);
			oowp+=iowp;

		oowp=oowp/(count[i][0]+count[i][1]);
#		print wp,owp,oowp
		print 0.25*wp+0.5*owp+0.25*oowp





	
