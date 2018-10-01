

def ok(ch) :
    return sorted(int(e) for e in ch)==list(int(e) for e in ch)

def previous(n) :
    return(list(e for e in l if int(e)<int(n))[-1])

n=int(input())
l=[str(e) for e in range(100) if ok(str(e))]

for nb in range(n) : 

	ch=input()
	#print(l)

	if not ok(ch) :
		if ch[1]==0 :
		    res="9"*len(ch)
		else :
		    res=previous(ch[:2])+"9"*(len(ch)-2)
	else :
		res=(ch)
	print("Case #"+str(nb+1)+":",res)
