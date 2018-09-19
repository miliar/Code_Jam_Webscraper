import sys
sys.path.append('/users/ahn/desktop/codejam/round 1B')

file = open('input.txt')

T = int(file.readline())

N = []
result = []
for i in range(0,T):
	result += [[]]

for i in range(0,T):
	N += [int(file.readline())]
	for j in range(0,N[i]):
		result[i] += [[[]]]
	for j in range(0,N[i]):
		temp = file.readline()
		for k in range(0,N[i]):
			result[i][j] += [temp[k]]
			
file.close()

WP = []
OWP = []
OOWP=[]
RPI = []
count = []
for i in range(0,T):
	WP += [[]]
	OWP += [[]]
	OOWP += [[]]
	RPI += [[]]
	count += [[]]
	
for i in range(0,T):
	for j in range(0,N[i]):
		WP[i] += [0]
		OWP[i] += [0]
		OOWP[i] += [0]
		RPI[i] += [0]
		count[i] += [0]
		
for i in range(0,T):
	for j in range(0,N[i]):
		count_all = 0
		count_win = 0
		for k in range(0,N[i]):
			if result[i][j][k+1] == '.':
				continue
			elif result[i][j][k+1] == '1':
				count_all+=1
				count_win+=1
			else:
				count_all+=1
		WP[i][j] = float(count_win)/float(count_all)
		count[i][j] = count_all
	for j in range(0,N[i]):
		WP_sum = 0.0
		for k in range(0,N[i]):
			if not result[i][j][k+1] == '.':
				if result[i][j][k+1] == '0':
					WP_sum += (WP[i][k]*float(count[i][k])-1)/float(count[i][k]-1)
				else:
					WP_sum += WP[i][k]*float(count[i][k])/float(count[i][k]-1)
		OWP[i][j] = WP_sum/float(count[i][j])
	for j in range(0,N[i]):
		OWP_sum = 0.0
		for k in range(0,N[i]):
			if not result[i][j][k+1] == '.':
				OWP_sum+=OWP[i][k]
		OOWP[i][j] = OWP_sum/float(count[i][j])
	for j in range(0,N[i]):
		RPI[i][j] = 0.25*WP[i][j] + 0.5 * OWP[i][j] + 0.25* OOWP[i][j]
		
output=''
for i in range(0,T):
	output += 'Case #'+str(i+1)+':\n'
	for j in range(N[i]):
		output += str(RPI[i][j])+'\n'

file = open('output.txt','w')
file.write(output)
file.close()