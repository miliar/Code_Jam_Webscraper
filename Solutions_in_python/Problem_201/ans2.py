from collections import defaultdict
for t in xrange(1,input()+1):
	n,k=map(int,raw_input().split())
	maximum,done=1,1
	current=defaultdict(lambda:0)
	current[n]=1
	while done<k:
		temp=defaultdict(lambda:0)
		for key,value in current.items():
			temp[(key-1)/2]+=(value)
			temp[key/2]+=(value)
		current=temp
		maximum<<=1
		done+=maximum
	previous=done-maximum
	blocks=current.keys()
	blocks.sort(reverse=True)
	for block in blocks:
		previous+=current[block]
		if previous>=k:
			print 'Case',('#'+str(t)+':'),block/2,(block-1)/2
			break
