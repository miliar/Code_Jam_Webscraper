#!/usr/bin/python

import sys

# main function
# write code from here
def process(input, output):
  nb = int(input.readline().rstrip())
  for val in range(1, nb+1):
    values = input.readline().rstrip().split()
    plug_size = int(values[0])
    fingers = int(values[1])

    elec = 0

    plugs = []
    for x in range(plug_size):
      plugs.append(False)

    for x in range(fingers):
      elec_changed = False

      for y in range(min(elec + 1, plug_size)):
        plugs[y] = not(plugs[y])
        if not plugs[y] and not elec_changed:
          elec = y
          elec_changed = True

      if not elec_changed:
        ind = elec
        while ind < plug_size and plugs[ind]:
          ind = ind + 1
        elec = ind

    if elec == plug_size:
      answer = "ON"
    else:
      answer = "OFF"

    output.write('Case #%d: %s\n' % (val,answer))

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "Need file as argument"
    sys.exit(1)

  input_file = sys.argv[1]

  # open the file
  input_handler = open(input_file, 'r')
  output_handler = open(input_file + '.out', 'w+')

  process(input_handler, output_handler)

  # close files
  input_handler.close()
  output_handler.close()
