f = open("B-large.in", 'r')
count = 0
content = f.read()
content = content.splitlines()
out = open("large-b-out", 'w')


def check(ss):
	new = ''.join(sorted(ss))
	if new == ss and int(new) <= int(ss):
		return True
	else:
		return False


for l in content:
	if count == 0:
		count += 1
		continue
	s = l
	if check(s):
		out.write("Case #" + str(count) + ': ' + s + '\n')
		count += 1
		continue
	for i in range(len(s)-1, 0, -1):
		new_s = str(int(s[0:i])-1) + '9' + s[i+1:len(s)]
		if check(new_s):
			out.write("Case #" + str(count) + ': ' + str(int(new_s)) + '\n')
			break
		else:
			s = new_s
	#out.write("Case #" + str(count) + ': ' + str(int(s)) + '\n')
	count += 1

