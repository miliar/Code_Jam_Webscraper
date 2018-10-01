from collections import OrderedDict

dic = OrderedDict([('a', 'y'), ('b', 'h'), ('c', 'e'), ('d', 's'), ('e', 'o'), ('f', 'c'), ('g', 'v'), ('h', 'x'), ('i', 'd'), ('j', 'u'), ('k', 'i'), ('l', 'g'), ('m', 'l'), ('n', 'b'), ('o', 'k'), ('p', 'r'), ('q', 'z'), ('r', 't'), ('s', 'n'), ('t', 'w'), ('u', 'j'), ('v', 'p'), ('w', 'f'), ('x', 'm'), ('y', 'a'), ('z', 'q'), (' ', ' ')])

def tr(line):
	global dic
	ans = ""
	line = line.strip()
	for i in line:
		ans += dic[i]
	return ans

fin = open("input.txt","r")
fout = open("output.txt","w")

ll = fin.readlines()
i = 1
for line in ll[1:]:
	fout.write( "Case #%d: %s\n" % (i,tr(line)) )
	i+=1
