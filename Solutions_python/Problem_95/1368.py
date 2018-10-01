import sys

inp = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv",]

out = ["our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up",]

map = {}

for i in range(0, 3):
	for j in range(len(inp[i])):
		map[inp[i][j]] = out[i][j]
map['q'] = 'z'
map['z'] = 'q'

#sorted = map.items()
#sorted.sort()

#print sorted

T = int(raw_input())
for i in range(1, T + 1):
	G = raw_input()
	print "Case #" + str(i) + ": ",
	for j in range(len(G)):
		sys.stdout.write(map[G[j]])
	print ''
