eng_to_goog = {'a': 'y', 'o': 'e', 'z': 'q', ' ': ' ', '\n': '\n'}
goog_to_eng = {'y': 'a', 'e': 'o', 'q': 'z', ' ': ' ', '\n': '\n'}

str1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
str2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
str3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

strs = [str1, str2, str3]

str1out = "our language is impossible to understand"
str2out = "there are twenty six factorial possibilities"
str3out = "so it is okay if you want to just give up"

strs_out = [str1out, str2out, str3out]

for i, s in enumerate(strs):
	for j, ch in enumerate(s):
		goog_to_eng[strs[i][j]] = strs_out[i][j]
		eng_to_goog[strs_out[i][j]] = strs[i][j]

alphabet = "abcdefghijklmnopqrstuvwxyz"

if len(goog_to_eng) == 27:
	for letter_key in alphabet:
		if letter_key not in goog_to_eng:
			for letter_val in alphabet:
				if letter_val not in eng_to_goog:
					goog_to_eng[letter_key] = letter_val
					eng_to_goog[letter_val] = letter_key 

# print len(eng_to_goog)
# print len(goog_to_eng)
# print goog_to_eng
# print eng_to_goog

def transformLine(s):
	ret = ''
	for ch in s:
		ret += goog_to_eng[ch]
	return ret

f1 = open('./A-small-attempt1.in', 'r')
f2 = open('./A-small-attempt1.out', 'w')
lines = f1.readlines()
for i, line in enumerate(lines):
	if not i == 0:
		temp = transformLine(line)
		f2.write("Case #" + str(i) + ": " + temp)

f1.close()
f2.close()

