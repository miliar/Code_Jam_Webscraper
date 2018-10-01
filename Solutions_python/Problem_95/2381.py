import string
import fileinput

mapping = {'a': 'y', 'o': 'e', 'z': 'q'}

test_ciphers = [
	'ejp mysljylc kd kxveddknmc re jsicpdrysi',
	'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
	'de kr kd eoya kw aej tysr re ujdr lkgc jv'
]
test_plains = [
	'our language is impossible to understand',
	'there are twenty six factorial possibilities',
	'so it is okay if you want to just give up'
]

c_alphabet = list(string.lowercase)
p_alphabet = list(string.lowercase)
c_alphabet.remove('y')
c_alphabet.remove('e')
c_alphabet.remove('q')
p_alphabet.remove('a')
p_alphabet.remove('o')
p_alphabet.remove('z')


for i in range(len(test_ciphers)):
	cipher = test_ciphers[i]
	plain = test_plains[i]
	for j in range(len(cipher)):
		c_char = cipher[j]
		p_char = plain[j]
		mapping[p_char] = c_char
		if c_char in c_alphabet:
			c_alphabet.remove(c_char)
			p_alphabet.remove(p_char)
			
if len(c_alphabet) == 1:
	mapping[p_alphabet[0]] = c_alphabet[0]

reverse_mapping = dict((v,k) for k,v in mapping.iteritems())

def decipher(text):
	result = ''
	for char in text:
		result += reverse_mapping[char]
		
	return result

f_in = open('A-small-attempt1.in', 'r')
f_out = open('A-small-attempt1.out', 'w')
lines = f_in.readlines()
i = 0
for l in lines:
	l = l.strip()
	i += 1
	if (i == 1):
		continue
	f_out.write('Case #'+str(i-1)+': ')
	f_out.write(decipher(l))
	f_out.write('\n')