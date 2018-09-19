frases=["ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"]
traduz=["our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"]
dic={'z':'q','q':'z'}
for i in range(len(frases)):
	for a in range(len(frases[i])):
		dic[frases[i][a]]=traduz[i][a]

for i in range(input()):
	g=raw_input()
	palavra=""
	for a in range(len(g)):
		palavra+=dic[g[a]]
	print "Case #" + str(i+1) + ': ' + palavra