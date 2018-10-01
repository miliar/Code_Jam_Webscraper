
f = open('btiny.in')
fout = open('btiny.out', 'w')
f = open('bsmall.in')
fout = open('bsmall.out', 'w')
# f = open('blarge.in')
# fout = open('blarge.out', 'w')

numCases = int(f.readline().strip())


def find_max(arr):
	maxI = None
	maxV = 0
	for i in range(len(arr)):
		if len(arr[i]) > maxV:
			maxI = i
			maxV = len(arr[i])

	return (maxI, maxV)

for numCase in range(numCases):
	print 'Case {}'.format(numCase + 1)

	ss = f.readline().strip().split(' ')
	N = int(ss[0])
	C = int(ss[1])
	M = int(ss[2])

	seats = []
	p_count = [0] * C

	for n in range(N):
		seats.append([])
	for m in range(M):
		ss = f.readline().strip().split(' ')
		pos = int(ss[0]) - 1
		person = int(ss[1]) - 1
		seats[pos].append(person)
		p_count[person] += 1

	max_p = max(p_count)

	# ret = max(p_count, max([len(a) for a in seats]))
	# changed = 0

	# for seat_no in range(1, N):
	# 	cnt = sum([len(a) for a in seats[0:seat_no+1]])

	# 	if cnt <= max_p * (seat_no+1):
	# 		continue
	# 	else:
	# 		evened = (cnt - 1) / (seat_no+1) + 1
	# 		if evened <= max_p:
	# 			pass
	# 		else:
	# 			max_seats = max(evened, max([len(a) for a in seats[seat_no+1:]]))
	# 			if max_seats <= max_p:
	# 				pass
	# 			else:
	# 				ret = max_seats

	# 				sums = 0

	changed = 0
	cnt = None
	print seats
	while True:
		(pos, cnt) = find_max(seats)
		print 'pos', pos, 'cnt', cnt, 'max_p', max_p
		if cnt <= max_p:
			break

		modif = False
		for i in range(0, pos):
			print 'seats[i]', i, seats[i]
			if len(seats[i]) < cnt-1:
				seats[i].append(seats[pos].pop())
				changed += 1
				modif = True
				break

		if modif:
			continue
		break


	fout.write('Case #{}: '.format(numCase + 1))
	fout.write('{} {}\n'.format(max(cnt, max_p), changed))


fout.close()

""" 	
 
5
2 2 2
2 1
2 2
2 2 2
1 1
1 2
2 2 2
1 1
2 1
1000 1000 4
3 2
2 1
3 3
3 1
3 3 5
3 1
2 2
3 3
2 2
3 1

Case #1: 1 1
Case #2: 2 0
Case #3: 2 0
Case #4: 2 1
Case #5: 2 1



"""

