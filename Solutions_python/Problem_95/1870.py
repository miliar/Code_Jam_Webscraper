import sys

if __name__ ==  "__main__":
	d = {'a':'y','o':'e','z':'q','q':'z','\n':''}
	s = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
	t = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
	for i in range(0, len(s)):
		d[s[i]] = t[i]
        input = sys.stdin.readlines()
	c = 1;
        for line in input[1:]:
		out = "Case #%d: " % c
		out = out + "".join([d[i] for i in line])
		print out
		c = c + 1
