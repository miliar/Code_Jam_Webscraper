matchInput = "q aoz our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
matchOutput = "z yeq ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"

def sort(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

f7in = sort(matchInput)
f7out = sort(matchOutput)

input = open('input.in', 'r')
out = open('output.txt', 'w')

i=0
output = ""

for line in input:
	if (i>0):
		output += "Case #" + str(i) + ": "
		for char in line:
			if char != "\n":
				output += f7in[f7out.index(char)]
		output += "\n"
	i=i+1

out.write(output)