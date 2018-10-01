#!/usr/bin/python -tt

ifile = open('./q2.in','r')
ofile = open('./q2.out','w')

def test(N, S, p, score, t):
	ans = 0
	for n in range(N):
		avg = score[n]/3
		mod = score[n]%3
		if avg >= p:
			ans += 1
		elif mod is 0 and S and avg+1 is p and score[n] is not 0:
			ans += 1
			S -= 1
		elif mod is 1 and avg+1 is p:
			ans += 1
		elif mod is 2 and avg+1 is p:
			ans += 1
		elif mod is 2 and S and avg+2 is p:
			ans += 1
			S -= 1

	ofile.write('Case #' + str(t+1) + ': ' + str(ans) + '\n')
	return

def main():

	T = int( ifile.readline() )

	for t in range(T):
		temp = []
		line = ifile.readline()
		for s in line.split():
			temp.append( int(s) )
		test(temp[0], temp[1], temp[2], temp[3:], t)
	print temp

if __name__ == '__main__':
	main()
