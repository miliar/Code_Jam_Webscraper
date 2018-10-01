import sys

tc = int(sys.stdin.readline())

for t in range(1,tc+1):
    string = sys.stdin.readline()[:-1]
    symbols = []
    dicsymbols = {}
    flag = 0
    count = 0
    for i in range(0,len(string)):
	if string[i] not in symbols:
	    symbols.append(string[i])
	    if i == 0:
		dicsymbols[string[i]] = 1
		count = count+1
	    elif flag == 0:
		#print dicsymbols
		dicsymbols[string[i]] = 0
		flag = 1
		count = count+1
	    else:
		dicsymbols[string[i]] = count
		count = count+1
#print dicsymbols
    base = len(symbols)
    if base == 1:
	base = 2
    answer = 0
#si = ''
    for i in string:
#si = si+str(dicsymbols[i])
	answer = answer*base+dicsymbols[i]
#print si
#print base
    print "Case #%d: %s" %(t,answer)
		
