#!/usr/bin/python

T = int(raw_input())
for t in xrange(T):
	N, K = tuple([int(item) for item in raw_input().split()])	
	f = []
	for i in xrange(N):
		f.append(raw_input())
	print "Case #%d:" % (t+1),

	# Processing
	for i in xrange(N):
		block = "".join(f[i].split('.'))
		f[i] = "."*(N - len(block)) + block

	win = {}
	for c in ["B", "R"]:
		win[c] = False
		for i in xrange(N):
			for j in xrange(N):
				# Down
				temp = ""
				for t in xrange(K):					
					if (i+t < N) and (j < N):
						temp += f[i+t][j]
				if (temp == c*K):
					win[c] = True

				# Right
				temp = ""
				for t in xrange(K):
					if (j+t < N) and (i < N):
						temp += f[i][j+t]
				if (temp == c*K):
					win[c] = True

				# R-Down
				temp = ""
				for t in xrange(K):
					if (i+t < N) and (j+t < N):
						temp += f[i+t][j+t]
				if (temp == c*K):
					win[c] = True

				# R-Up
				temp = ""
				for t in xrange(K):
					if (i-t >= 0) and (j+t < N):
						temp += f[i-t][j+t]
				if (temp == c*K):
					win[c] = True

		
	if win["B"]:
		if win["R"]:
			print "Both"
		else:
			print "Blue"
	else:
		if win["R"]:
			print "Red"
		else:
			print "Neither"
			