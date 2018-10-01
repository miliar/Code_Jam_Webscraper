#!/usr/bin/python

case = "large"
input_file = "B-%s.in" % case
output_file = "B-%s.out" % case

fin = open(input_file)
fout = open(output_file, "w")

n = int(fin.readline().strip())

for z in range(1, n+1):
	t = int(fin.readline().strip())
	na, nb = [int(x) for x in fin.readline().strip().split()]
	da = []
	for i in range(na):
		l = [x.split(":") for x in fin.readline().strip().split()]
		da += [(int(l[0][0])*60 + int(l[0][1]), int(l[1][0])*60 + int(l[1][1]))]
	db = []
	for i in range(nb):
		l = [x.split(":") for x in fin.readline().strip().split()]
		db += [(int(l[0][0])*60 + int(l[0][1]), int(l[1][0])*60 + int(l[1][1]))]
	da.sort()
	db.sort()
	#print da
	#print db
	arra = []
	arrb = []
	ta, tb = 0, 0
	tsa, tsb = 0, 0
	while len(da) > 0 or len(db) > 0:
		s = min(da + db)
		ta += len([g for g in arra if g <= s[0]])
		arra = [g for g in arra if g > s[0]]
		tb += len([g for g in arrb if g <= s[0]])
		arrb = [g for g in arrb if g > s[0]]
		#print ta, tb, arra, arrb, s
		#print da, db
		if len(da) > 0 and s == da[0]:
			if ta == 0:
				ta += 1
				tsa += 1
			ta -= 1
			arrb += [s[1]+t]
			da = da[1:]
		else:
			if tb == 0:
				tb += 1
				tsb += 1
			tb -= 1
			arra += [s[1]+t]
			db = db[1:]
	print >> fout, "Case #%d:" % z, tsa, tsb

fin.close()
fout.close()
