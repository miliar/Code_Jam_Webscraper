f = open("A-large.in",'r')
o = open("output.out",'w')

for i in range(1):
	test = f.readline()

for case in range(int(test)):
	in_string = f.readline()
	a = in_string.split(" ")
	d = int(a[0])
	listo = []
	for num in range(int(a[1])):
		inp = f.readline()
		b = inp.split(" ")
		dist = float(d - int(b[0]))
		sp = float(int(b[1]))
		t = dist / sp 
		listo.append(t)
	listo.sort()
	ti = listo[int(a[1]) - 1]
	if ti > 0:
		spee = float(d) / ti
	else:
		spee = 0	
	o.write("case #" + str(case + 1)+": "+str(spee)+ "\n")

f.close()
o.close()