import sys

if __name__=="__main__" :
	l=['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']
	t = int(raw_input())

	for i in range(t) :
		data = str(raw_input())
		sys.stdout.write("Case #"+str(i+1)+": ")
		for c in data :
			if c==' ' :
				sys.stdout.write(" ")
			else :
				sys.stdout.write(l[ord(c)-ord('a')])
		sys.stdout.write("\n")
