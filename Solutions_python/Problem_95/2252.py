from __future__ import print_function
fh=open('/home/valek/python/A-small-attempt1.in','r')
out=open('/home/valek/python/A-small-practise-output.txt','w')
dictionary={'y':'a','n':'b','f':'c','i':'d','c':'e','w':'f','l':'g','b':'h','k':'i','u':'j','o':'k','m':'l','x':'m','s':'n',
'e':'o','v':'p','z':'q','p':'r','d':'s','r':'t','j':'u','g':'v','t':'w','h':'x','a':'y','q':'z'," ":" ",'\n':'\n'}
n=fh.readline()
char=str()
for i in xrange(int(n)):
	line=fh.readline()
	for sentense in xrange(len(line)):
		char+=dictionary[line[sentense]]
	out.write("Case #{0}: " "{1}".format(i+1,char))
	char=str()
fh.close()
out.close()
	
	
