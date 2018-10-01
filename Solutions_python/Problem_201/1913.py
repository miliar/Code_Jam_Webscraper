def longest_seq(_list):
	count, prev, index = 0, 0, 0
	for i in range(0,len(_list)):
		if _list[i] == 0:
			count += 1
		else:
			count = 0
		if count > prev:
		        prev = count
		        index = i
	return (index-prev, prev, int(prev/2), prev - int(prev/2) -1)


file_in = 'C-small-1-attempt2.in'
file_out = 'out.txt'
with open(file_in,'rb') as fin, open(file_out,'w') as fout:
	lines = fin.read().splitlines()
	case = 1
	for l in lines[1:]:
		print (l)
		i = int(l.split()[0])
		n, k = int(l.split()[0]), int(l.split()[1])

		bathrooms_status = [0] * (n+2)
		bathrooms_status[0], bathrooms_status[n+1] = 1, 1

		for i in range(k):
			index, count, _max, _min = longest_seq(bathrooms_status)
			# print(str(index) + "/" + str(count) + "\t" + str(_max) + "/" + str(_min))
			bathrooms_status[index + int((count+1)/2)] = 1
			# print(bathrooms_status)


		output = 'Case #%d: %d %d\n' % (case,_max, _min)
		fout.write(output)
		case += 1


