import math
import sys

def get_map():
	file_read = open("1_map.txt", 'r')
	lines = file_read.readlines()	
	g_word = [] ; e_word = [] ; lang_map = {}
	for k in range(3):	
		g_word.append(str(lines[2*k]))
		e_word.append(str(lines[(2*k)+1]))
		
		for j in range(len(g_word[k])):
			val = e_word[k][j] ; key = g_word[k][j]
			if key not in lang_map.keys():
				lang_map[key] = val
	
	lang_map['\n'] = ''
	lang_map['z'] = 'q'
	lang_map['q'] = 'z'

	return lang_map

def translate(word, lang_map):
	new_word = ''
	for k in range(len(word)):
		new_word = new_word + lang_map[word[k]]
	return new_word

def main():
	file_read = open(sys.argv[1], 'r')
	lines = file_read.readlines()	
	no_test_cases = int(lines[0])
	lang_map = get_map()
	for k in range(no_test_cases):		
		word = lines[k+1]
		new_word = translate(word, lang_map)
		print "Case #" + str(k+1) + ":",
		print new_word

if __name__ == '__main__':
	main()