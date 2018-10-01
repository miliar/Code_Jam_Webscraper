fi = open("input.txt", "r+")
fo = open("output.txt", "r+")

cases = int(fi.readline().strip())

for c in range(cases):
	caseStr = "Case #" + str(c + 1) + ": "
	rules = map(int, fi.readline().strip().split())
	nomino = rules[0]
	l = rules[1]
	w = rules[2]

	if nomino == 1:
		fo.write(caseStr + "GABRIEL\n")
	elif nomino == 2:
		if (l * w) % 2 == 0:
			fo.write(caseStr + "GABRIEL\n")
		else:
			fo.write(caseStr + "RICHARD\n")
	elif nomino == 3:
		if l == 1 or w == 1:
			fo.write(caseStr + "RICHARD\n")
		else:
			if (l * w) % 3 == 0:
				fo.write(caseStr + "GABRIEL\n")
			else:
				fo.write(caseStr + "RICHARD\n")
	elif nomino == 4:
		if l == 1 or w == 1:
			fo.write(caseStr + "RICHARD\n")
		elif (l * w) % 4 != 0:
			fo.write(caseStr + "RICHARD\n")
		elif l == 2 or w == 2:
			fo.write(caseStr + "RICHARD\n")
		else:
			fo.write(caseStr + "GABRIEL\n")