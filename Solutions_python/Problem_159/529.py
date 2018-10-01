for t in range(0, int(input())):

	n = int(input())
	mush = [int(x) for x in input().split()]

	t_1 = 0
	m_diff = 0
	t_2 = 0
	for m in range(1, n):
		if mush[m] < mush[m-1]:
			t_1 += mush[m-1] - mush[m]
		if mush[m-1] - mush[m] > m_diff:
			m_diff = mush[m-1] - mush[m]
	
	for m in range(0, n-1):
		if mush[m] <= m_diff:
			t_2 += mush[m]
		else:
			t_2 += m_diff


	print("Case #%d: %d %d" %(t+1, t_1, t_2))