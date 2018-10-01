#p='A-small-practice.in'
p='A-small-attempt0.in'
in1 = open(p,'r')
T = in1.readline()
for t in range(int(T)):
	answer1 = int(in1.readline().strip())
	r1=[[0,0,0,0]]*4
	r1[0] = map(int,in1.readline().strip().split())
	r1[1] = map(int,in1.readline().strip().split())
	r1[2] = map(int,in1.readline().strip().split())
	r1[3] = map(int,in1.readline().strip().split())
	
	answer2 = int(in1.readline().strip())
	r2=[[0,0,0,0]]*4
	r2[0] = map(int,in1.readline().strip().split())
	r2[1] = map(int,in1.readline().strip().split())
	r2[2] = map(int,in1.readline().strip().split())
	r2[3] = map(int,in1.readline().strip().split())
	
	s=set(r1[answer1-1]) & set(r2[answer2-1])
	l = len(s)
	if l==1:
		print 'Case #{}: {}'.format(t+1, s.pop())
	if l>1:
		print 'Case #{}: {}'.format(t+1, 'Bad magician!')
	if l==0:
		print 'Case #{}: {}'.format(t+1, 'Volunteer cheated!')
#print 'Case #{}: Draw'.aformat(inx+1, )
in1.close()	