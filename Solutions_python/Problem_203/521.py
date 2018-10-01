def solve(cake, r, c) :
	empty_line = 0
	l = []
	for i in range(0,r) :
		a = ''
		empty_char = 0
		for j in range(0,c) :
			if cake[i][j] == '?'  :
				if a != '' :
					cake[i][j] = a
				else :
					empty_char += 1
			else :
				a = cake[i][j]
				if empty_char > 0 :
					for k in range(1, empty_char+1) :
						cake[i][j-k] = a
					empty_char = 0
		if a == '' :
			if l != [] :
				cake[i] = l
			else :
				empty_line += 1
		else :
			l = cake[i]
			for j in range(1, empty_line+1) :
				cake[i-j] = l
			empty_line = 0
	return cake

t = int(input())
for i in range(0,t) :
	r, c = input().split()
	r = int(r)
	c = int(c)
	cake = []
	for j in range(0,r):
		cake += [list(input())]
	result = solve(cake, r, c)
	print("Case #", i+1, ":", sep="")
	for j in result :
		l = ""
		print("".join(j))