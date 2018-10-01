import pickle

def parse_sample_lines():
	input = open('input1.txt', 'rb')
	output = open('output1.txt', 'rb')
	hash = {'y': 'a', 'q': 'z', 'e': 'o'} 
	length = int(input.readline())

	for _ in range(length):
		i_line = input.readline()
		o_line = output.readline()

		for idx in range(len(i_line)):
			hash[i_line[idx]] = o_line[idx]

	with open('hash.txt', 'w') as f:
		pickle.dump(hash, f)

def convert_googlerese():
	with open('hash.txt', 'r') as f:
		h = pickle.load(f)

	outstring = ''
	with open('input.txt', 'rb') as input:
		length = int(input.readline())
		for i in range(length):
			outstring += "Case #%i: " % (int(i)+1)
			line = input.readline()
			for c in line:
				try:
					outstring += h[c]
				except KeyError:
					outstring += 'q'

	print outstring
	with open('output.txt', 'w') as outf:
		outf.write(outstring)

if __name__ == "__main__":
	convert_googlerese()
