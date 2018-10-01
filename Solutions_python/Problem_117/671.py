def canbedone(m, n, lawn):
    max_row = [0] * n
    max_column = [0] * m
    for row in range(n):
	for column in range(m):
	    v = lawn[row][column]
	    if max_row[row] < v:
                max_row[row] = v
	    if max_column[column] < v:
		max_column[column] = v
    for row in range(n):
	for column in range(m):
	    v = lawn[row][column]
	    if max_row[row] > v and max_column[column] > v:
		return False
    return True

file_prefix = 'B-large'
input_file = file_prefix + '.in'
output_file = file_prefix + '.out'

def main():
    ifs = open(input_file, 'rb')
    ofs = open(output_file, 'wb')
    itr = iter(ifs)
    t = int(itr.next().strip())
    for i in range(t):
        dim = map(int, itr.next().strip().split())
        n, m = dim[0], dim[1]
        lawn = []
        for j in range(n):
            row = map(int, itr.next().strip().split())
            lawn.append(row)
        ofs.write('Case #%d: %s\n' % (i + 1,
                                    "YES" if canbedone(m, n, lawn) else "NO"))

if __name__ == '__main__':
    main()
