#from hints + no q in sample data and no z (only one left)
mapping = {'a':'y', 'o':'e', 'z':'q', 'q':'z'}

def build_map(input, output, mapping):
	for i in range(len(input)):
		for j in range(len(input[i])):
			mapping[input[i][j]] = output[i][j]
	return mapping

def translate(sentence, mapping):
    out = ""
    for c in sentence:
        out = out + mapping[c]
    return out

test_data_in = [
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"
]

test_data_out = [
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"
]

mapping = build_map(test_data_in, test_data_out, mapping)
    
def solve_lines(lines, mapping):
    tests = int(lines[0])
    out = ""
    for i in range(1,tests+1):
        out = out + "Case #" + str(i) + ": "
        out = out + translate(lines[i], mapping)
        out = out + "\n"
    return out

def solve_file(filename, mapping):
    f = open(filename)
    l = []
    for line in f:
        l = l + [line[:-1]]
    f.close()
    return solve_lines(l,mapping)
    
ans = solve_file("A-small-attempt0.in", mapping)

out = open('A-out', 'w')
out.write(ans)
out.close()