def is_tidy(nbInput):
	nombre = str(nbInput)

	last_char = nombre[0]

	for char in nombre:
		if char < last_char:
			return 0
		last_char = char

	return 1

def traiterCas(nombre):
	last = 0
	nombre = int(nombre)

	i=1
	while i <= nombre:
		#print i
		if is_tidy(i):
			last = i
		i = i+1

	return last

t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
	nombre = raw_input()
	print "Case #%d: %d" % (i, traiterCas(nombre))