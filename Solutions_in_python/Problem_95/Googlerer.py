# -*- coding: utf-8 -*-

alphabet = dict({'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'})

with open('input.txt') as f:
	f_out = open('output.txt', 'w')
	t = int(f.readline())
	for i in range(t):
		text = f.readline().split(' ')
		ans = []
		for word in text:
			ans_word = ''
			for char in word:
				if char in alphabet:
					ans_word += alphabet[char]
				else:
					ans_word += char
			ans.append(ans_word)
		f_out.write('Case #{0}: {1}'.format(i+1, ' '.join(ans)))
	f_out.close()
