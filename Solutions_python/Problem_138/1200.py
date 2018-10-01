f=open('D-large.in','r')
f2=open('Dlarge.out','w')
import math
numTest=int(f.readline())

for i in range(1,numTest+1):
	numBlocks=int(f.readline())
	Naomi=[float(x) for x in f.readline().split()]
	Ken=[float(x) for x in f.readline().split()]
	Naomi.sort()
	Naomi.reverse()
	Naomi2=list(Naomi)

	Ken.sort()
	Ken.reverse()
	Ken2=list(Ken)

	score1_ken=0
	for j in range(0,numBlocks):
		chosen_naomi=Naomi.pop()
		chosen_ken=0
		while (chosen_ken<chosen_naomi and len(Ken)>0):
			chosen_ken=Ken.pop()
		if(chosen_ken>chosen_naomi):
			score1_ken+=1
	score1_naomi=numBlocks-score1_ken


	score2_naomi=0
	for j in range(0,numBlocks):
		chosen_ken2=Ken2.pop()
		chosen_naomi2=0
		while (chosen_naomi2<chosen_ken2 and len(Naomi2)>0):
			chosen_naomi2=Naomi2.pop()
		if(chosen_naomi2>chosen_ken2):
			score2_naomi+=1


	f2.write("Case #"+str(i)+": "+str(score2_naomi)+" "+str(score1_naomi)+"\n")




