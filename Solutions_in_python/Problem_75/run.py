import sys

inputFile = sys.stdin
count = int(inputFile.readline())

lineno = 1
for line in inputFile:
  row = line.split()
  row.reverse()

  c_num = int(row.pop())
  c = []

  for i in xrange(c_num) :
    c.append(row.pop())

  d_num = int(row.pop())
  d = []
  
  for i in xrange(d_num) :
    d.append(row.pop())

  input_num = row.pop()
  input = row.pop()
  output = []

  for i in xrange(len(input)):
    output.append(input[i])

    if len(output) > 1:
      for cur_c in c:
        if (output[-1] == cur_c[0] and output[-2] == cur_c[1]) or \
           (output[-1] == cur_c[1] and output[-2] == cur_c[0]):
          output.pop()
          output.pop()
          output.append(cur_c[2])

      for cur_d in d:
        for j in output:
          if (j == cur_d[0] and output[-1] == cur_d[1]) or \
             (j == cur_d[1] and output[-1] == cur_d[0]):
            output = []
            break;

  print "Case #%d:" % lineno,

  print '[' + ', '.join(output) + ']'
  
  lineno += 1
