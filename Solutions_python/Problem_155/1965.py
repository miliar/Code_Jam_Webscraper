import sys

if __name__ == '__main__':
	fp = sys.argv[1]
	with open(fp) as f:
		case_num = 1
		for case in f:
			line_s = case.strip().split(' ')
			if len(line_s) == 1:
				continue

			s_max = line_s[0]
			audience = list(line_s[1])

			n = 0
			s = 0
			additional_n = 0
			while s < len(audience):
				if s > n:
					additional_n += 1
					n += 1
				n += int(audience[s])
				s += 1

			print "Case #" + str(case_num) + ": " + str(additional_n)
			case_num += 1