
firstin = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
firstout = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

alphabet='abcdefghijklmnopqrstuvwxyz'
code   = 'ejpmyslckdxvnribtahwfougqz'
decode = 'ourlangeismpbtdhwyxfckjvzq'
def crack(inp,outp,alphabet):
	i = 0
	inp = inp.replace(' ','')
	outp = outp.replace(' ','')
	red = []
	red2 = []
	red3 = []
	code = alphabet
	for c in inp:
		if(not red.__contains__(c)):
			red.append(c)
			red3.append(outp[i])
			if(not red2.__contains__(outp[i])):
				red2.append(outp[i])
				code = code.replace(outp[i],c)
			#print code
			#print c+'|'+outp[i]
		#print red
		i = i + 1
	print ''.join(red)
	print ''.join(red2)
	print ''.join(red3)
	return code
	
def IsCompleteAlpha(inp):
	red = []
	inp = inp.replace(' ','')
	for c in inp:
		if(not red.__contains__(c)):
			red.append(c)
	print sorted(red)
	print len(red)
	if(len(red)==26):
		return True
	return False

def dec(inp,code,decode):
	clear = ''
	for c in inp:
		if(not code.__contains__(c)):
			clear = clear + c
		else:
			clear = clear + decode[code.find(c)]
	print clear
	return clear

#IsCompleteAlpha(firstin)
#code = crack(firstin,firstout,alphabet)
#print alphabet
#print code 
dec(firstin,code,decode)
