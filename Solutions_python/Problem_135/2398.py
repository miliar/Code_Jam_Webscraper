N_ROWS = 4

ipt = open('A-small-attempt0.in').read().splitlines()

cases = int(ipt[0])

base = 1

f = open('A-small-attempt0.out','w')

for x in xrange(cases):

	guess1 = int(ipt[base])
	guess_row1 = ipt[base + guess1].split(' ')
	guess2 = int(ipt[base+5])
	guess_row2 = ipt[base + guess2 + 5].split(' ')

	intersection = list(set(guess_row1).intersection( set(guess_row2)))
	cnt = len(intersection)
	if cnt == 1:
		msg = intersection[0]
	elif cnt == 0:
		msg = "Volunteer cheated!"
	elif cnt > 1:
		msg = "Bad magician!"

	case_num = x+1

	f.write("Case #{0}: {1}\n".format(case_num, msg))

	base+= 10

f.close()