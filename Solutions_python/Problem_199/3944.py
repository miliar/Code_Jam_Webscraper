import sys
f=open(sys.argv[1],'r')
n=int(f.readline())

def solver(inn,meg):
	level=0
	appeared={inn:True}
	currgen=[inn]
	nextgen=[]
	while currgen:
		for tr in currgen:
			if tr.count('+')==len(tr):
				return level
			for i in range(0,len(tr)-meg+1):
				nb=tr[:i]+(((tr[i:i+meg].replace('+','e')).replace('-','+')).replace('e','-'))+tr[i+meg:]
				if not nb in appeared:
					appeared[nb]=True
					nextgen.append(nb)
		level+=1
		currgen=nextgen
		nextgen=[]

	return 'IMPOSSIBLE'

for i in range(n):
	inp,meg=f.readline().split(' ')
	meg=int(meg)
	# print inp,meg
	print 'Case #{0}:'.format(i+1),solver(inp,meg)
