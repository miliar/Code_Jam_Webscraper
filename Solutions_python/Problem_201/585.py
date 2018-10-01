t = int(input())

for case in range(1,t+1):
	n,k = [int(i) for i in input().split()]

	big = n
	big_n = 1
	sml = n
	sml_n = 0
	while k > big_n + sml_n:
		k -= big_n + sml_n
		tmp1 = sml_n*2 if sml&1 else sml_n
		tmp2 = big_n*2 if big&1 else big_n
		tmp1 += big_n if not big&1 else 0
		tmp2 += sml_n if not sml&1 else 0
		sml_n, big_n = tmp1, tmp2
		sml, big = (sml-1)//2, big//2
		# print(sml, big)
		# print(sml_n, big_n)
	
	if k <= big_n:
		ans = big
	elif k <= big_n + sml_n:
		ans = sml
	print('Case #%d: %d %d' % (case, ans//2, (ans-1)//2))
