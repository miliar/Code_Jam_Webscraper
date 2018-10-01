def stats(number):
	# number is string.
	dict = {'0': 0,
			'1': 0,
			'2': 0,
			'3': 0,
			'4': 0,
			'5': 0,
			'6': 0,
			'7': 0,
			'8': 0,
			'9': 0
			}
	for letter in list(number):
		dict[letter]+=1
	return dict

def bla(number):
	print number
	offline = False
	nlist=[]
	for p in all_perms(list(number)):
		if p[0]!="0":
			nlist.append("".join(p))
	nlist.sort()
	#print nlist
	index = nlist.index(number)
	#print "Index:", index, "num:",nlist[index]
	while nlist[index]==number:
		index+=1
		#print "Index:", index, "num:",nlist[index], "len:",len(nlist)
		if index == len(nlist):
			break
	if index == len(nlist):
		l = []
		for k in all_perms(list(number+'0')):
			if k[0]!="0":
				l.append("".join(k))
		l.sort()
		
		yield "Case #%d: %s\n" % (i+1,l[0])
	else:
		yield "Case #%d: %s\n" % (i+1, nlist[index])

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]


f = open("B-small-attempt1.in")
#f = open("A-small-attempt0.in")
g= open("output.txt","w")
numline=int( f.readline().strip("\n"))
for i in range(numline):
	number = f.readline().strip("\n")
	for response in bla(number):
		g.write(response)
g.close()

