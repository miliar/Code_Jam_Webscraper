t = int(raw_input())
for tc in xrange(t):
	print "Case #"+str(tc+1)+":",
	
	#Code Begins
	n = int(raw_input())
	str_n = str(n)
	str_len = len(str_n)
	loop_cont = True

	while(loop_cont):
		for i in xrange(1,str_len):
			if str_n[i-1] > str_n[i]:
				loop_cont = True
				n = n -1
				str_n = str(n)
				str_len = len(str_n)
				break
			else:
				pass
		else:
			loop_cont = False

	print n