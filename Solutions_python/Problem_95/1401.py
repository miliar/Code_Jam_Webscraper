map = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', ' ':' '}

def convert_to_english(text):
	result = ""
	for char in text:
		result += map[char]
	return result
	
def print_output():
	i = 1
	fin = open("A-small-attempt1.in.txt", "r")
	fout = open("output.txt", "w")
	lines = fin.read().split('\n')[1:]
	for line in lines:
		result = convert_to_english(line)
		print "Case #" + str(i) + ": " + result
		fout.write("Case #" + str(i) + ": " + result + '\n')
		i += 1
		
print_output()