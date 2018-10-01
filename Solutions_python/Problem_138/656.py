import string

file = 'D-large'
# file = 'test4'
input = open(file+'.in','r')
output = open(file+'.out','w')

t = int(input.readline())
for casecount in range(t):
	n = int(input.readline())
	nao = sorted([float(s) for s in string.split(input.readline(), ' ')])
	backup_nao = nao
	ken = sorted([float(s) for s in string.split(input.readline(), ' ')])
	backup_ken = ken

	index1, index2, ans1, ans2 = 0, 0, 0, 0

	for num in nao:
		if num > ken[index2]:
			ans1 += 1
			index2 += 1

	for num in nao:	
		if num > ken[-1]:
			ken = ken[1:]
			ans2 += 1
		else:
			pick = min([k for k in ken if k > num])
			ken = [k for k in ken if k != pick]
	
	output.write('Case #'+str(casecount+1)+': '+str(ans1)+' '+str(ans2)+'\n')