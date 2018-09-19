import math
input_file = open("ex.in")

output_file = open('ex.out', 'w')
def next_line():
	return input_file.readline()
def test_farms(ammount, C, F, X):
	prod = 2
	secs = 0
	if ammount == 0:
		return X/prod
	for x in range(ammount):
		secs += C / prod
		prod = prod + F
	secs += X / prod
	return secs
cases = int(next_line())
for case_number in range(cases):
	N = int(next_line())
	p1 = []
	p2 = []
	p12 = []
	p22 = []
	for n in next_line().split():
		p1.append(float(n))
		p12.append(float(n))
	for n in next_line().split():
		p2.append(float(n))
		p22.append(float(n))
	p=0
	for i in range(N):
		if max(p1)>min(p2):
			p+=1
			p1.sort()
			for i in range(len(p1)):
				if p1[i]>min(p2):
					p1.pop(i)
					break
			p2.pop(p2.index(min(p2)))
		else:
			p1.pop(p1.index(min(p1)))
			p2.pop(p2.index(max(p2)))

	output_file.write('Case #'+str(case_number+1)+': '+str(p))

	p=0
	for i in range(N):
		if max(p12)>max(p22):
			p+=1
			p12.pop(p12.index(max(p12)))
			p22.pop(p22.index(min(p22)))
		else:
			p22.sort()
			for i in range(len(p22)):
				if p22[i]>max(p12):
					p22.pop(i)
					break
			p12.pop(p12.index(max(p12)))
	output_file.write(' '+str(p)+'\n')
