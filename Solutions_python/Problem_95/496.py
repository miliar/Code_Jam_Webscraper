#!/usr/bin/python

import sys


def process(input, output):
  nb = int(input.readline().rstrip())
  
  for val in range(1, nb+1):
    
    print("Case ",val)
    
    # reading data
    inputs = input.readline().rstrip()
    
    d = {'q':'z','z':'q','a': 'y', ' ': ' ','h':'x','f':'c','b':'h','i':'d', 'c': 'e', 'e': 'o', 'd': 's', 'g': 'v', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}

    answer=''
    for letter in inputs:
      try:
        answer += d[letter]
      except KeyError:
        answer += 'X'
        d[letter]=' '
        
    output.write('Case #%d: %s\n' % (val,answer))
    print(sorted(d.values()))

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Need file as argument")
    sys.exit(1)

  input_file = sys.argv[1]

  # open the file
  input_handler = open(input_file, 'r')
  output_handler = open(input_file + '.out', 'w+')

  process(input_handler, output_handler)

  # close files
  input_handler.close()
  output_handler.close()
