import sys
def main():
	f=open(sys.argv[1])
	N=int(f.readline())
	I=0
	while N:
		I+=1
		N-=1
		S=int(f.readline())
		names=[]
		while S:
			S-=1
			names.append(f.readline())
		Q=int(f.readline())
		words=[]
		while Q:
			Q-=1
			words.append(f.readline())
		print "Case #%d: %d"%(I,solve(names,words))

def solve(names,words,lastName=None):
	res=0
	while 1:
		try:
			index,name=max([(words.index(name),name) for name in names if name!=lastName])
		except ValueError:
			return res
		res+=1
		words=words[index+1:]
		lastName=name
if __name__=="__main__":
	main()
