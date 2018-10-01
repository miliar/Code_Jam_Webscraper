for case in range(1, int(input())+1):
	print("Case #%d:" % (case))
	(R,C) = list(map(int,input().split()))
	npending = 0
	pending = True
	s = ""
	for r in range(R):
		cr = list(input())
		i = 0
		while ((i < C) and (cr[i] == "?")):
			i += 1
		if (i < C):
			for j in range(i):
				cr[j] = cr[i]
			i += 1
			while (i < C):
				if (cr[i] == "?"):
					cr[i] = cr[i-1]
				i += 1
			s="".join(cr)
			if (pending):
				for j in range(npending):
					print(s)
				pending=False
			print(s)
		else:
			if (pending):
				npending += 1
			else:
				print(s)
			

