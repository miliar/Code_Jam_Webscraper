eng = "aozq our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
goog = "yeqz ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"

out = {}

def translate(text):
	result = ""
	for i in range(len(text)):
		if (text[i] == " "):
			result = result + " "
		else:
			result = result + chr(out[ord(text[i])])
	return result

for i in range(len(eng)):
	out[ord(goog[i])] = ord(eng[i])

counter = 0;
output = open('outputA.txt', 'w')
with open('inputA.txt', 'r') as f:
	for fileLine in f:
		if (counter == 0):
			counter = counter + 1
			continue
		output.write("Case #" + str(counter) + ": " + translate(fileLine.rstrip()) + "\n")
		counter = counter + 1

f.close()
output.close()
