f=open('A-small-attempt1.in')
d={'\n':'\n',' ':' ','y':'a','n':'b','f':'c','i':'d','c':'e','w':'f','l':'g','b':'h','k':'i','u':'j','o':'k','m':'l','x':'m','s':'n','e':'o','v':'p','z':'q','p':'r','d':'s','r':'t','j':'u','g':'v','t':'w','h':'x','a':'y','q':'z'}
l=[]
l1=int(f.readline())
def c(l):
	r=''
	for i in l:
		r=r+i.replace(i,d[i])
	return r
for i in range(l1):
	l.append(c(f.readline()))
f.close()
outf=open('A-small-attempt1.out','w')
for n,i in enumerate(l):
	print 'Case #%s: %s'%(n+1, i)
	l='Case #%s: %s'%(n+1, i)
	outf.write(l+'\n')
outf.close()	
 
