import sys

translation_dict = {' ': ' ',
                    'a': 'y',
                    'b': 'h',
                    'c': 'e',
                    'd': 's',
                    'e': 'o',
                    'f': 'c',
                    'g': 'v',
                    'h': 'x',
                    'i': 'd',
                    'j': 'u',
                    'k': 'i',
                    'l': 'g',
                    'm': 'l',
                    'n': 'b',
                    'o': 'k', 
                    'p': 'r', 
                    'q': 'z',
                    'r': 't',
                    's': 'n', 
                    't': 'w',
                    'u': 'j', 
                    'v': 'p', 
                    'w': 'f', 
                    'x': 'm',
                    'y': 'a',
                    'z': 'q', 
                    }
                    

filename = sys.argv[1]
data = open(filename, 'r')
output = open('output.dat', 'w')

n_cases = int(data.readline())

for i in range(n_cases):
  line = data.readline().rstrip()
  outline = ""
  for char in line:
    outline += translation_dict[char]
  output.writelines('Case #'+str(i+1)+': '+outline+'\n')