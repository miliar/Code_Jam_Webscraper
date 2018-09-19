def answer(x,r,c):
	if r*c % x != 0:
		return 'RICHARD'
	if x == 1 or x == 2:
		return 'GABRIEL'
	if (x == 4) and ((r*c == 12) or (r*c == 16)):
		return 'GABRIEL'
	if (x == 3) and r*c > 3:
		return 'GABRIEL'
	else:
		return 'RICHARD'

lines = [line.strip() for line in open('in')]
n = lines[0]

for i in range(int(n)):
	case = lines[i+1].split()
	x = int(case[0]); r = int(case[1]); c= int(case[2])
	ans = answer(x,r,c)
	print('Case #' + str(i+1) + ': ' + ans)

