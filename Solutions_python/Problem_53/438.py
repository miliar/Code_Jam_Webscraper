maxk = [0,1];
for i in range(2,31):
	maxk.append(maxk[i-1]*2+1);

t = int(raw_input());
case = 1;
while t-case+1:
	line = raw_input().split(' ')
	n = int(line[0])
	k = int(line[1])
	if ((k+1) % (maxk[n]+1)) == 0:
		result = 'ON'
	else:
		result = 'OFF'
	print 'Case #%i: %s' % (case, result)
	case=case+1;
	