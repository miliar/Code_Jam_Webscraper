input = open('allyour.txt', 'r')
output = open('allyourans.txt', 'w')

def base10(x, b):
	ans = 0
	s = str(x)
	for i in xrange(len(s)):
		ans += int(s[-(i+1)])* (b**i)
	return ans

T = input.readline()
for t in xrange(int(T)):
	s = input.readline()
	if s[-1] == '\n':
		s = s[:-1]
	used = [s[0]]
	abc = {}
	abc[s[0]] = 1
	k = 0
	while  k< len(s):
		if s[k] == s[0]:
			k +=1
		else:
			break
	if k < len(s):
		abc[s[k]] = 0
		used.append(s[k])
	k = 2
	for i in s:
		if i not in used:
			abc[i] = k
			k += 1
			used.append(i)
	numb = []
	for i in xrange(len(s)):
		numb.append(abc[s[i]])
	numb = map(str, numb)
	numb = ''.join(numb)
	numb = int(numb)
	base = len(abc)
	if base == 1:
		base = 2
	ans = base10(numb, base)
	output.write('Case #' + str(t+1) + ': ' + str(ans) + '\n')

input.close()
output.close()