# Oversized Pancake Flipper
# suhas kashyap
# kashyap 07
# kashyapsuhas07@gmail.com

def foo(N):
	flips = 0
	sequence = list(N[0])
	k = int(N[1])

	for side in range(len(sequence)-(k-1)):
		if sequence[side] == '-':
			flips = flips + 1
			for cap in range(k):
				if sequence[side+ cap] == '-':
					sequence[side + cap] = '+'
				else:
					sequence[side + cap] = '-'

	# what am i doing
	flag = False

	for j in sequence:
		if j == '+':
			pass
			continue
		else:
			flag = True
			break
		break

	if flag == True:
		print('Case #', i+1, ': ', 'IMPOSSIBLE', sep='')
	else:
		print('Case #', i+1, ': ', flips, sep='')


if __name__ == "__main__":
	T = int(input())	# T test cases
	N = [] *T 			# N Number
	for i in range(T):
		N.append(input().split(' '))
	for i in range(T):
		foo(N[i])