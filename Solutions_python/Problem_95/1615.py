myfile = open("A-small-attempt0.in", 'r')
f = myfile.readlines()
outfile = open('output.out', 'w')

d = {}
d[' '] = ' '
d['a'] = 'y'
d['o'] = 'e'
d['z'] = 'q'
allchar = set("abcdfghijklmnopqrstuvwxz")
count = 1

for line in range(len(f)):
	str1 = "our language is impossible to understand"
	str2 = "there are twenty six factorial possibilities"
	str3 = "so it is okay if you want to just give up"
	if line == 0:
		continue
	if line == 1:
		for char in range(len(f[line].strip())):
			d[f[line][char]] = str1[char]
			allchar = allchar.difference(set(f[line][char]))
			continue
	if line == 2:
		for char in range(len(f[line].strip())):
			d[f[line][char]] = str2[char]
			allchar = allchar.difference(set(f[line][char]))
			continue
	if line == 3:
		for char in range(len(f[line].strip())):
			d[f[line][char]] = str3[char]
			allchar = allchar.difference(set(f[line][char]))
			continue
	d['q'] = 'z'
	outfile.write("Case #%d: " %count)
	realstring = ''
	for i in f[line].strip():
		realstring += d[i]

	outfile.write("%s\n" %realstring)
	count += 1
