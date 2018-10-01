mappings = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm', 'y': 'a', 'z': 'q', ' ': ' '}

def translate(input):
	output = ""
	for c in input:
		output += mappings[c]
	return output

def main():	
	for T in xrange(int(raw_input())):
		print 'Case #{0}: {1}'.format(T+1, translate(raw_input()))

if __name__ == '__main__':
	main()

