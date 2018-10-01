import sys
buf=[]
def scans():
    global buf
    while 1:
        while len(buf) <= 0:
            buf=input().replace('\n',' ').split(' ')
        o=buf.pop(0)
        if o!='':
            break
    return o
def scan():
    return int(scans())
def scanf():
    return float(scans())

sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')
for t in range(1,1+scan()):
	n = scan()
	naomi = [scanf() for i in range(n)]
	kenji = [scanf() for i in range(n)]
	naomi.sort();kenji.sort()

	# wars
	count = 0
	naomic,kenjic=naomi[:],kenji[:]
	for i in range(n):
		i=naomic[i]
		for k,j in enumerate(kenjic):
			if j>i:
				kenjic.pop(k)
				break
		else:
			kenjic.pop(0)
			count+=1
	# print(naomi);print(kenji)
	# D wars
	countd = 0
	for i in range(n):
		told = kenji[-1]
		i=naomi[i]
		if(told < i):
			told = i
		if(i>kenji[0]):
			told = kenji[-1]+1
		for k,j in enumerate(kenji):
			if j>=told:
				kenji.pop(k)
				break
		else:
			kenji.pop(0)
			countd+=1

	print("Case #%d: %d %d"%(t,countd,count))