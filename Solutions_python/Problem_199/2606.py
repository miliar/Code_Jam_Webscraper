import sys


def parseCase(fin):
	line = next(fin).strip()
	row, k = line.split(' ')
	return row, int(k)

def solve(row, k):
	row = [ch == '+' for ch in row]
	n = len(row)
	count = 0
	while not all(row):
		firstFalse = row.index(False)
		if firstFalse > n-k:
			return "IMPOSSIBLE"
		else:
			for j in range(k):
				#print(firstFalse,j,k,(n-k+1))
				row[firstFalse+j] = not row[firstFalse+j]
			count += 1

	return count


def main(filenameIn, filenameOut):
	with open(filenameIn, 'rt') as fin, open(filenameOut, 'wt') as fout:
		line = next(fin).strip()
		count = int(line)
		for i in range(count):
			row, k = parseCase(fin)
			answer = solve(row, k)
			fout.write("Case #{}: {}\n".format(i+1, answer))

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
