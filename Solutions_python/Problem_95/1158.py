from sys import stdin
f = open('output.out', 'w')

mapping = {'y':'a','e':'o','q':'z', 'z':'q'}


reese = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',\
		'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',\
		'de kr kd eoya kw aej tysr re ujdr lkgc jv']

eng = ['our language is impossible to understand',\
		'there are twenty six factorial possibilities',\
		'so it is okay if you want to just give up']

for i in range(len(reese)):
	for j in range(len(reese[i])):			
			mapping[reese[i][j]] = eng[i][j]

for i in range(int(stdin.readline())):
	google = stdin.readline()
	google = google[0:len(google)-1]
	english = ''
	for j in google:
		english += (mapping[j])
	
	print 'Case #'+str(i+1)+': ' + english
	f.write('Case #'+str(i+1)+': ' + english + '\n')

f.close()