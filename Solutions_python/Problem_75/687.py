import sys

def do_line(line, case_num):
	print line
	unprocessed = line.split(' ')
	num_replace = int(unprocessed[0])
	unprocessed = unprocessed[1:]
	
	replacements = {}
	print "Finding", num_replace, "replaces"
	for i in range(num_replace):
		A, B, R = unprocessed[i]
		replacements["%s%s" % (A, B)] = R
		replacements["%s%s" % (B, A)] = R
	print replacements
	unprocessed = unprocessed[num_replace:]
	num_nukes = int(unprocessed[0])
	unprocessed = unprocessed[1:]
	print "Finding", num_nukes, "nukes"
	nukes = {}
	for i in range(num_nukes):
		A, B = unprocessed[i]
		nukes["%s%s" % (A, B)] = True
		nukes["%s%s" % (B, A)] = True
	unprocessed = unprocessed[num_nukes:]
	print nukes

	num_input = int(unprocessed[0])
	print "Finding", num_input, "inputs"
	unprocessed = unprocessed[1]

	elm = []
	for i in range(num_input):
		elm.append(unprocessed[i])
		if len(elm) >= 2 and "%s%s" % (elm[-2], elm[-1]) in replacements:
				elm = elm[:-2] + [replacements["%s%s" % (elm[-2], elm[-1])]]
		conts = {}
		for e in elm:
			conts[e] = True
		for k,v in conts.iteritems():
			for l,w in conts.iteritems():
				if "%s%s" % (k, l) in nukes:
					elm = []
					break
	return ''.join(elm)


in_, out_f= sys.argv[1], sys.argv[1]+".out"
out = open(out_f, 'w')
with open(in_, 'r') as file:
	file.next()
	num = 1
	for line in file:
		ret = do_line(line, num)
		out.write("Case #%d: [%s]\n" % (num, ', '.join(ret)))
		num += 1
