reader = lambda:map(float, raw_input().split())
for ti in xrange(input()):
	C,F,X = reader()
	Ans = X / 2.0
	Now = 2.0
	Cnt = 0
	while Cnt<=Ans:
		Cnt = Cnt + (C / Now)
		Now = Now + F
		if(Cnt + (X / Now) < Ans):
			Ans = Cnt + (X / Now)
	print "Case #%d:" % (ti + 1),
	print "%.8f" % Ans
		
	