#Python3.0

L, D, N=map(int, input().split())
out=open("out","w")
dict_words=[input() for i in range(D)]

#Read in and split
seqs=[]
for i in range(N):
	st=input()
	seq=[]
	bin=None
	for c in st:
		if c=="(":
			bin=[]
		elif c==")":
			seq.append(set(bin))
			bin=None
		elif bin==None:
			seq.append(c)
		else:
			bin.append(c)
	seqs.append(seq)

#Match
for i, seq in enumerate(seqs):
	cnt=0
	for dict_word in dict_words:
		for letter, opts in zip(dict_word, seq):
			if not letter in opts:
				break
		else:
			cnt+=1
	out.write("Case #"+str(i+1)+": "+str(cnt)+"\n")