from math import log, ceil


fin = open('input.in', 'r')
lines = iter(fin.readlines())
fin.close()
lines.next()
fout = open('out.txt', 'w+')

for num, line in enumerate(lines):
	n, k = map(int, line.split())
	blah = int(ceil(log(k,2)))

	lis = [n]
	dic = {n: 1}

	while True:
		m = max(lis)
		many = dic[m]
		dic.pop(m)
		if k <= many:
			m -= 1
			break

		k -= many
		lis.remove(m)
		m -= 1
		halfup = m - m/2
		halfdown = m/2

		if halfup == halfdown:
			if halfup in dic:
				dic[halfup] += many*2
			else:
				dic[halfup] = many*2
			if halfup not in lis:
				lis.append(halfup)
		else:
			if halfup in dic:
				dic[halfup] += many
			else:
				dic[halfup] = many
			if halfdown in dic:
				dic[halfdown] += many
			else:
				dic[halfdown] = many
			if halfup not in lis:
				lis.append(halfup)
			if halfdown not in lis:
				lis.append(halfdown)

	fout.write('Case #%s: %s %s\n' %(str(num+1), str(m - m/2), str(m/2)))

fout.close()