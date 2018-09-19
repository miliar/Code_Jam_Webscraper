from __future__ import with_statement

def process_case(data, out):
    memo = {}
    def match(s, m):
	if (s, m) in memo:
	    return memo[(s, m)]
	if len(m) == 0:
	    return 1
	if len(m) > len(s):
	    return 0
	if s[0] != m[0]:
	    return match(s[1:], m)
	elif s[0] == m[0]:
	    memo[(s, m)] = match(s[1:], m[1:]) + (match(s[1:], m))
	    return memo[(s, m)]

    w = data.readline().strip("\n")
    out.write("%04d\n" % (match(w, "welcome to code jam") % 10000))

def process_file(fname):    
    
    with open(fname, "r") as data:
	with open("answer_" + fname, "w") as answer:
	    n = int(data.readline().strip("\n"))
	    for i in range(n):
		answer.write("Case #%d: " % (i+1))
		process_case(data, answer)
process_file("C-large.in")