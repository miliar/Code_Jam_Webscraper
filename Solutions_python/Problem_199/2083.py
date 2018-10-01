import sys

def main():
    f = open(sys.argv[1])
    t = int(f.readline().strip())

    for i in xrange(t):
	line = f.readline().strip()
	sp = line.split()
	ss = [c for c in sp[0]]
	n = int(sp[1])

	flag = True
	ind =0
	res = 0

	while ind < len(ss):
	    if ss[ind] == "-":
		if len(ss) - ind < n:
		    flag = False
		    break

	    	for pos in xrange(ind, ind+n):
		    if ss[pos] == "-":
			ss[pos] = "+"
		    else:
			ss[pos] = "-"
		res += 1
	    
	    ind += 1

	if flag:
	    print "Case #"+str(i+1)+": "+str(res)
	else:
	    print "Case #"+str(i+1)+": IMPOSSIBLE"


    f.close()

if __name__ == "__main__":
    main()
