
list={}
list={' ':' ','y':'a','n':'b','f':'c','i':'d','c':'e','w':'f','l':'g','b':'h','k':'i','u':'j','o':'k','m':'l','x':'m','s':'n','e':'o','v':'p','z':'q','p':'r','d':'s','r':'t','j':'u','g':'v','t':'w','h':'x','a':'y','q':'z'}
a=open("in.txt","r")
b=a.read()
b=b.split('\n')
w=open("out","w")
z=1
ct=b[0]
while 1:
	e=b[z]
	ans=""
	for i in e:
		ans+=list[i]
	l="Case #"+str(z)+": "+ans+"\n"
	
	w.write(l)
	z+=1
	if z==len(b) or z==ct:break
w.close()
a.close()
