#!/usr/bin/python

def main():
	m = {}
	s1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'
	s2 = 'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'
	for i in xrange(len(s1)):
		m[s1[i]] = s2[i]
	m['\n'] = '\n'
	m["z"] = "q"
	m["q"] = "z"
	
	file_in = open("A.in", "r")
	file_out = open("A.out", "w")

	for i in xrange(int(file_in.readline())):
		line = file_in.readline()
		outline = ''
		for c in line:
			outline += m[c]

		file_out.write("Case #%s: %s" % (i + 1, outline))

	file_in.close()
	file_out.close()

if __name__ == "__main__":
	main()
