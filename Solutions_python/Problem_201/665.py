T = int(input())
for t in range(1,T+1):
	N,K = map(int,input().split())
	def half(X):
		return X//2, X - X//2 -1 
	elements = [N]
	counts = {N:1}
	pointer = 0
	total_count = 1
	def insert(X, times):
		global total_count
		total_count += times
		try:
			counts[X] += times
		except:
			counts[X] = times
			elements.append(X)	
	while total_count != 2*N+1 :
		a , b = half(elements[pointer])
		times = counts[elements[pointer]]
		pointer += 1	
		insert(a, times)
		insert(b, times)

	cum_sum = 0
	for e in elements:
		cum_sum += counts[e]
		if cum_sum >= K:
			answer = half(e)
			break

	print('Case #{}: {} {}'.format(t,answer[0],answer[1]))