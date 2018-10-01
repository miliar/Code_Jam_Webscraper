def items():
  return raw_input().split()

num_cases = int(items()[0])

for case_num in xrange(1, num_cases + 1):
  tmp = items()
  C = int(tmp[0])
  combs = tmp[1:C+1]
  D = int(tmp[C+1])
  oppos = tmp[C+2:C+D+2]
  N = int(tmp[C+D+2])
  elems = tmp[C+D+3:C+D+N+3][0]
  answer = [elems[0]]
  for i, elem in enumerate(elems[1:]):
    answer.append(elem)
    if len(answer) > 1:
      if (answer[-1] in ''.join(combs)) & (answer[-2] in ''.join(combs)):
        for x, comb in enumerate(combs):
          if (answer[-1] in comb[0:2]) & (answer[-2] in comb[0:2]) & ((answer[-1] != answer[-2]) | (comb[0] == comb[1])):
            answer[-2:] = comb[-1]
            break
      for oppo in oppos:
        if (oppo[0] in answer) & (oppo[1] in answer):
          answer = []
          break
  
  print "Case #%d: [%s]" % (case_num, ', '.join(map(str, answer)))

