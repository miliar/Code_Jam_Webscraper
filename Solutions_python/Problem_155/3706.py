with open('p1input.txt', 'r') as content_file:
    content =  [i.strip() for i in content_file.readlines()]
data = []
content.pop(0)
for i in content:
	data.append(i.split(' '))
	data[-1][0] = int(data[-1][0])

print data
toinvite = 0
standing = 0

with open('p1solution.txt', 'w') as f:
	for shyness, aud in enumerate(data):
		toinvite = 0
		standing = 0	
		audience = map(int, list(aud[1].strip()))
		for index, mem in enumerate(audience):
			if mem == 0:
				pass
			elif standing >= index:
				standing += mem
			else:
				toinvite += index - standing 
				print toinvite
				standing += mem 
				standing += toinvite
		#if toinvite > 0:
		f.write("Case #%s: %s" % ((shyness+1), toinvite))
		#else:
		#	f.write("Case #%s: 0" % (shyness+1))
		f.write('\n')

f.close()