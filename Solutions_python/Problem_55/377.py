for c in xrange(int(raw_input())): # For each test case
	r,k,n=map(int,raw_input().split())
	groups=map(int,raw_input().split())
	mon=[] # The amount of money aquired if this group is at the front of the queue
	ski=[] # The next group that'll  be a the front of the queue if this one is
	for i in xrange(len(groups)): #Precalculating
		money=0
		on=i
		while (money+groups[on]<=k and (on!=i or money==0)): #while the amount of people on the ride is less than the max and we haven't included all the people
			money+=groups[on]
			on=(on+1)%len(groups)
		mon.append(money)
		ski.append(on)
	
	lcost=[0]*len(groups)
	llength=[-1]*len(groups)
	looplen=0
	loopcost=0
	on=0 #start at the beggining
	while llength[on]==-1:
		llength[on]=looplen
		lcost[on]=loopcost
		looplen+=1
		loopcost+=mon[on]
		on=ski[on]
	loopcost-=lcost[on]
	looplen-=llength[on]
	
	cost=0
	if llength[on]>r:
		#Do stuff without loops and stuff
		on=0
		while r>0:
			cost+=mon[on]
			on=ski[on]
			r-=1
	else:
		r-=llength[on]
		cost+=lcost[on]
		cost+=loopcost*(r/looplen)
		r=r%looplen
			
		while r>0:
			cost+=mon[on]
			on=ski[on]
			r-=1
	print "Case #"+str(c+1)+":",cost
