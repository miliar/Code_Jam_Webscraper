#R = 5  #The roller coaster will run R times in a day.
#k = 5  #The roller coaster can hold k people at once
#N = 10 #N space-separated integers gi
#T = 1 #the number of test cases, T.

f = open('C-small-attempt0.in','r')
output = open('fo.txt','w')
fin = f.readlines()
tmpT = fin[0].split('\n')
T = int(tmpT[0])

for t in range(1,T+1):
	i_index1 = 2*t-1
	i_index2 = 2*t 
	tmp_1 = fin[i_index1].split('\n')
	tmptmp_1 = tmp_1[0].split(' ')
	[R,k,N] = [int(tmptmp_1[0]),int(tmptmp_1[1]),int(tmptmp_1[2])]
	tmp_2 = fin[i_index2].split('\n')
	tmptmp2 = tmp_2[0].split(' ')
	g = []
	for comp in tmptmp2:
		g.append(int(comp))
	
	
	#g = [2,4,2,3,4,2,1,2,1,3]
	index =0;
	tmpSum = 0;
	totalPeople = 0;
	for i in range(1,R+1): # total run R times
		tmpSum = 0
		cnt = 1
		while tmpSum <= k:
			tmpSum = tmpSum + g[index%N]
			index = (index +1)%N
			cnt = cnt +1
			if tmpSum >k:
				index = (index-1)%N
				tmpSum = tmpSum - g[index]
				break
			if cnt>N:			
				break

		totalPeople = totalPeople + tmpSum;
	output.write('Case #')
	output.write(str(t))
	output.write(': ')
	output.write(str(totalPeople))
	output.write('\n')