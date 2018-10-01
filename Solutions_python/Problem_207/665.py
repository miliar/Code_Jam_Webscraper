def solve():
	f = open('input.in','r')
	w = open('output.out','w')
	test = int(f.readline())
	for i in range(1,test+1):





		answerString = ""
		numbers = list(map(int,f.readline().split()))
		n = numbers[0]
		bnumbers = [[numbers[1],'R'],[numbers[3],'Y'],[numbers[5],'B']]
		bnumbers.sort(reverse=True)
		numbers = bnumbers[0][1]
		answerString+=bnumbers[0][1]
		bnumbers[0][0]-=1






		while bnumbers[0][0]>0 or bnumbers[1][0]>0 or  bnumbers[2][0]>0:
		    bnumbers.sort(reverse=True)
		    j=0
		    if numbers==bnumbers[j][1]:
		        j+=1
		    if bnumbers[j][0]==0:
		        answerString="IMPOSSIBLE"
		        break
		    numbers = bnumbers[j][1]
		    answerString+=bnumbers[j][1]
		    bnumbers[j][0]-=1
		if answerString!="IMPOSSIBLE" and answerString[0]==answerString[-1]:
		    if answerString[-1]!=answerString[-3]:
		        answerString = answerString[:-2] + answerString[-1]+answerString[-2]
		    else:
		        answerString="IMPOSSIBLE"

		w.write('Case #{}: {}\n'.format(i,answerString))

	f.close()
	w.close()
solve()
