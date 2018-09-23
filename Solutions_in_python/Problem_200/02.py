input_name = "example" 
input_name = "B-small-attempt0" 
input_name = "B-small-attempt1" 
inputs = list()
solutions = list()

# input
fi = open(input_name + '.in', 'r')
# fi.readline()
for line in fi:
  inputs.append(int(line.strip()))

cases = inputs[1:]
print 'Cases: ', cases

# solution
for x in range(0, len(cases)):
  sep = list(str(cases[x]))
  # print sep, sorted(sep)
  if (sep == sorted(sep)):
    solutions.append(cases[x])
  else:
    print "Searching", cases[x]
    case = list(str(cases[x]))
    quick = list()

    decrease = 1
    rcase = case[::-1]
    # print rcase
    for y in range(0, len(rcase)):
      if (y == 0):
        quick.append(str('9'))
        continue
      if (y == len(rcase) - 1):
        if (decrease == 1): 
          quick.append(str(int(rcase[y]) - 1))
        else:
          quick.append(str(int(rcase[y])))
        continue
      if (decrease == 1): 
        print rcase[y], rcase[y + 1]
        if (int(rcase[y]) - int(rcase[y + 1]) <= 0):
          quick.append(str('9'))
        else:
          quick.append(str(int(rcase[y]) - 1))
          decrease = 0
      else:
        quick.append(str(int(rcase[y])))
    solutions.append(int(''.join(quick[::-1])))
    print rcase, quick


print 'Solutions: ', solutions

# output
fo = open(input_name + '.out', 'w')
for x in range(0, len(solutions)):
  fo.write('Case #' + str(x + 1) + ': ' + str(solutions[x]) + '\n')

# closure
fi.close()
fo.close()