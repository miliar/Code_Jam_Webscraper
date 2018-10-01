#!/usr/bin/python

import sys

# main function
# write code from here
def process(input, output):
  nb = int(input.readline().rstrip())
  for val in range(1, nb+1):
    # reading data
    inputs = input.readline().rstrip().split()

    nbGooglers = int(inputs[0])
    nbSurprising = int(inputs[1])
    p = int(inputs[2])
    results = inputs[3:]

    minNonSurprising = p*3 - 2
    minSurprising = p*3 - 4

    if minSurprising < 0:
      minSurprising = minNonSurprising

    answer = 0

    for x in results:
      v = int(x)
      if (v >= minNonSurprising):
        answer += 1
      elif (nbSurprising > 0 and v >= minSurprising):
        nbSurprising -= 1
        answer += 1

    output.write('Case #%d: %s\n' % (val,answer))

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
