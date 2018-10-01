

f = open("A-small-attempt0.in","r")
wf = open("A-small-attempt0.out","w")


def main():
	T = int(f.readline())
	for case in range(1,T+1):
		start(case)
	f.close
	wf.close

def start(case):
	name, n = [i for i in f.readline().split()]
	n, nvalues = int(n), 0
	for i in range(len(name)+1):
		for j in range(i,len(name)+1):
			nvalues += count(name[i:j], n)
	wf.write("Case #{}: {}\n".format(case,nvalues))
	
	
	
def count(s, n):
	vowels = [ 'a', 'e', 'i', 'o', 'u' ]
	cons = 0	
	for i in s:
		if cons == n:
			return 1
		if i not in vowels:
			cons += 1
		else:
			cons = 0
	if cons == n:
		return 1
	return 0
	

if __name__ == '__main__' :
	main()	




