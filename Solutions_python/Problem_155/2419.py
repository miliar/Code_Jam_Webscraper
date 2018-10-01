T=int(raw_input())
for t in range (T):
	ind,arr=raw_input().split()
	ind = int (ind)
	arr1 = map(int,arr)
	sum_ctr,req_ctr = 0,0
	for i in range(ind+1):
		if arr1[i] <> 0:
			if sum_ctr < i:
				req_ctr +=  i - sum_ctr
				sum_ctr = i 
			sum_ctr += arr1[i]
	print "Case #%d:"%(t+1),req_ctr
