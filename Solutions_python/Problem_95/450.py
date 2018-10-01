from sys import argv

samples = {"ejp mysljylc kd kxveddknmc re jsicpdrysi" : "our language is impossible to understand",
			"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" : "there are twenty six factorial possibilities",
			"de kr kd eoya kw aej tysr re ujdr lkgc jv" : "so it is okay if you want to just give up"
		}
		
char_map = {}

for coded, actual in samples.items():
	for i, c in enumerate(coded):
		if c in char_map and char_map[c] != actual[i]:
				print("WTF")
		char_map[c] = actual[i]

char_map['z'] = 'q'
char_map['q'] = 'z'

def translate(s):
	global char_map
	res = ""
	for c in s:
		res += char_map[c]
	return res

index = 0
for line in open(argv[1]):
	if index != 0:
		print("Case #" + str(index) + ": " + translate(line.strip()))
	index += 1