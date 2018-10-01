def parse(input):
  config = input.readline()
  ldn = config.split()
  d = []
  print ldn
  for line in range(int(ldn[1])):
    d += [ input.readline().strip() ]

  output = open('data.out', 'w')
  for (number, line) in enumerate(input.readlines()):
    case = "".join(["Case #", str(number + 1), ": ", str(test(d, line.strip())), '\n'])
    print case.strip()
    output.write(case)
  output.close()

def test(d, line):
  words = []
  prepare = line.split(')')
  for word in prepare:
    if word.find('(') >= 0:
      if word.find('(') == 0:
        words += [word[1:]]
      else:
        words += word[0:word.find('(')]
        words += [word[word.find('(') + 1:]]
    elif len(word) > 0:
      words += word

  print words
  print ""

  count = 0
  for v in d:
    increase = True
    for index in range(len(v)):
      if words[index].find(v[index]) < 0:
        increase = False
        break

    if (increase == True):
      count += 1

  return count
    
try:
  input = open('data.in', 'r')
  parse(input)
  input.close()
except IOError:
  print "Can't open input file."