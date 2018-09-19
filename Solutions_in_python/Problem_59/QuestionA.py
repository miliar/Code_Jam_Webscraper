import sys

infile = open('A-large.in', 'r');
outfile = open('Aout-large' + ".out", 'w');
cases = int(infile.readline());

class Node:
    def __init__(self, name, parent):
        self.name = name;
        self.parent = parent;
	self.children = [];

for case in range(1,cases+1):
	ans = 0;
	line = infile.readline().rstrip("\n\r").split();
	N = int(line[0]);
	M = int(line[1]);
	
	root = {};
	for i in range(0,N):
		dirs = infile.readline().rstrip("\n\r").split('/');
		node = root;
		for u in dirs:
		    try:
			if u != '':
			    if u not in node:
				node[u] = {};
			node = node[u];
		    except:
			print '';
	#print root

	for i in range(0,M):
		dirs2 = infile.readline().rstrip("\n\r").split('/');
		node = root;
		for u in dirs2:
		    try:
			#print u
			if u != '':
			    if u not in node:
				node[u] = {};
				ans+=1;
				#print "added ",u
			node = node[u];
		    except:
			print '';
	#print root
	ans = str(ans);

	print "Case #" + str(case) + ": " + str(ans)
	outfile.write("Case #" + str(case) + ": " + str(ans) + "\n");

outfile.close();