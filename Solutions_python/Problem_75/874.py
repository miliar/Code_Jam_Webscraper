def do_oppose():
	global oppose, final
	for v in oppose:
		if (v[0] in final and final[-1] == v[1]) or (v[1] in final and v[0] == final[-1]):
			final = []
			break

def do_combo():
	global combo, final
	if len(final) > 1:
		for v in combo:		
			if len(final) > 1:
				if (final[-2] == v[0] and final[-1] == v[1]) or (final[-2] == v[1] and final[-1] == v[0]):
					del final[-1]
					del final[-1]
					final.append(v[2])	
					
	
f = open("input.txt", "r")
w = open("output.txt", "w")

cases = int(f.readline())
combo, oppose, invoke, final = [],[],[],[]

for case in range(1, cases+1):
	combo, oppose, invoke, final = [],[],[],[]
	parts = f.readline().strip().split(' ')
	C = int(parts[0])
	for c in range(0, C):
		combo.append(list(parts[c+1]))
	D = int(parts[C+1])
	for d in range(0, D):
		oppose.append(list(parts[C+2+d]))
	invoke = parts[-1]

	for i in invoke:
		final.append(i)
		do_combo()
		do_oppose()		
	#print "Case #%d: [%s]" % (case, ', '.join(final))
	w.write("Case #%d: [%s]\n" % (case, ', '.join(final)))
f.close()
w.close()