def rf(n, d):
    '''Reduces fractions. n is the numerator and d the denominator.'''
    def gcd(n, d):
        while d != 0:
            t = d
            d = n%d
            n = t
        return n
    assert d!=0, "integer division by zero"
    assert isinstance(d, int), "must be int"
    assert isinstance(n, int), "must be int"
    greatest=gcd(n,d)
    n/=greatest
    d/=greatest
    return [n, d]

filename = input("Enter file name of test case: ")
rfname = input("Enter result file name: ")
file = open(filename)

ipt = file.readlines()
ls = int(ipt[0])

res = []

for n in range(1,ls+1):
	a = ipt[n]
	a = a.split()
	
	for i in range(len(a)):
		a[i] = int(a[i])
	
	r=[]
	for i in range(1,a[0]+1):
		if (a[1]/100)*i == round((a[1]/100)*i):
			q = ((a[1]/100)*i)/i
			r.append(rf(int(100*q),100))
	print(n,r)
	
	if len(r) == 0:
		res.append("Broken")
		continue
	
	s=[]
	for i in r:
		if (100-a[2] < i[1]-i[0]):
			s.append(1)
		elif (i[0] > 0 and a[2] == 0):
			s.append(1)
			
	if len(s)!=len(r):
		res.append("Possible")
	else:
		res.append("Broken")
	
	
tostr = ""
for n in range(len(res)):
	tostr+="Case #" + str(n+1) + ": " + str(res[n]) + "\n"
	
rfile = open(rfname, 'w')
rfile.write(tostr[:-1])
s=input("Die Zeit ist um.")