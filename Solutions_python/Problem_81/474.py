#!/usr/bin/python

T=input()

for SPM in range(T):

	opponent=[]

	n=input()

	matr=[]

	for loop in range(n):
		line=raw_input()
		temp=[]
		for k in line:
			if k==".":
				temp.append(2)
			else:
				temp.append(int(k))
			

		matr.append(temp)

	#print "Matrix : ", matr

	#creating opponent list
	opponent_list=[]

	for k in range(n):
	
		temp=[]
		for p in range(n):
			if matr[k][p]!=2:
				temp.append(p)
			if matr[p][k]!=2:
				temp.append(p)
		temp=sorted(list(set(temp)))

		opponent_list.append(temp)	

	#print "opponent_list :",opponent_list

	#opponent_list done


	# Calculate the WP of all teams
	def win_point(matr):

		WP=[]

		for k in matr:

			total=0
			win=0
		 	loss=0

			for p in k:
				if p==1:
					win+=1
					total+=1
				elif p==0:
					loss+=1
					total+=1
			if total>0:		
				win_percent=float(win)/total
			else:
				win_percent=0

			WP.append(win_percent)

	
		return WP

	WP=win_point(matr)

	#calculating the OWP

	OWP=[]

	for k in range(n):

	
		#copying matr into back

		back=[]

		for k1 in matr:
			t=[]
			for p in k1:
				t.append(p)
			back.append(t)

		#copying end
	
	
		for p in range(n):
			back[p][k]=2
			back[k][p]=2

		temp_win=win_point(back)
		#print k,"   ",temp_win	
		sum=0
		count=0
		average=0

		for p in opponent_list[k]:
			sum+=temp_win[p]
			count+=1

		if count>0:
			OWP.append(float(sum)/count)
		else:
			OWP.append(0)


	#print OWP
		

	# calculate OOWP

	OOWP=[]

	for k in range(n):
		sum=0
		count=0	
	
		for p in opponent_list[k]:
			sum+=OWP[p]
			count+=1

		if count>0:
			OOWP.append(float(sum)/len(opponent_list[k]))
		else:
			OOWP.append(0)
 			

	#print OOWP

	RPI=[]

	for k in range(n):
		val=0.25*WP[k]+0.50*OWP[k]+0.25*OOWP[k]
		RPI.append(val)

	print "Case #%d:"%(SPM+1)
	
	for k in range(n):
		print RPI[k]



				