def main(filein, fileout):
	with open(filein) as f:
		num_cases = int(f.readline())
		output = [0] * num_cases
		for case, line in enumerate(f):
			params = line.split()
			max_s = int(params[0])
			total_aud = 0
			for k, aud in enumerate(params[1]):
				total_aud += int(aud)
				if total_aud + output[case] < k + 1:
					output[case] += k + 1 - total_aud - output[case]
	write_to_file(fileout, output)

def write_to_file(filename, output):
	with open(filename, 'w') as f:
		for i, out in enumerate(output):
			f.write('Case #%d: %d\n'%(i+1, out))

if __name__ == '__main__':
	main('A-large.in', 'codejam_qual_alarge.out')