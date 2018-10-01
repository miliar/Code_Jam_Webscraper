#!/usr/bin/python3

words = []
class InvalidWord(Exception): pass

def parseLanguage(data):
	pattern = []
	position = 0
	while position < len(data):
		if data[position] == '(':
			end = data.index(')', position);
			pattern.append(list(data[position+1:end]))
			position = end+1
		else:
			pattern.append(list(data[position]))
			position += 1
	return pattern


def isValidWord(pattern):
	matches = 0
	#print("Got", pattern)
	global words
	for word in words:
		try:
			#print("Trying", word)
			for char in range(len(word)):
				if word[char] not in pattern[char]:
					#print(word[char], "does not match", pattern[char])
					raise InvalidWord
			#print("We got this far")
			matches += 1
		except InvalidWord:
			pass
	return matches

def main():
	global words
	patterns = []
	matches = []
	fin = open("A-large.in")
	line = fin.readline().split()
	L = int(line[0])
	D = int(line[1])
	N = int(line[2])
	lines = fin.readlines()
	words = [line.strip() for line in lines[:D]]
	#print(words)
	patterns = [parseLanguage(line.strip()) for line in lines[D:]]
	#print(patterns)
	for pattern in patterns:
		matches.append(isValidWord(pattern))
	for i in range(len(matches)):
		print("Case #" + str(i+1) + ": " + str(matches[i])) 
if __name__=="__main__":
	main()
