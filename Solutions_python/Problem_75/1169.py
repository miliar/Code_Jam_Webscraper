def task (i, case):
  values = case.split(" ")

  combine = {}
  combine['Q'] = {}
  combine['W'] = {}
  combine['E'] = {}
  combine['R'] = {}
  combine['A'] = {}
  combine['S'] = {}
  combine['D'] = {}
  combine['F'] = {}

  n = int(values.pop(0))
#  print n, "combines"

  for _ in range(n):
    comb = values.pop(0)
#    print comb
    combine[comb[0]][comb[1]] = comb[2]
    combine[comb[1]][comb[0]] = comb[2]

  n = int(values.pop(0))
#  print n, "opposes"

  opposed = {}
  opposed['Q'] = []
  opposed['W'] = []
  opposed['E'] = []
  opposed['R'] = []
  opposed['A'] = []
  opposed['S'] = []
  opposed['D'] = []
  opposed['F'] = []

  for _ in range(n):
    op = values.pop(0)
#    print op
    opposed[op[0]].append(op[1])
    opposed[op[1]].append(op[0])

  n = values.pop(0)
#  print n, "invokes"

  invokes = values.pop(0).strip()
#  print "invokes:", invokes

  el_list = []
  for inv in invokes:
    #print "\n", el_list
    #print "inv=", inv
    done_combine=False
    for comb in combine[inv].keys():
#      if comb in el_list:
#      print "comb=", comb
#      print "ultimo da lista: ", el_list[-1:]
      if [comb] == el_list[-1:]:
        el_list.pop()
        el_list.append(combine[inv][comb])
        done_combine=True

    done_oppose=False
    if not done_combine:
      for opp in opposed[inv]:
#        print "trying", opp, "for opposed to ", inv
        if opp in el_list:
          el_list = []
          done_oppose=True
    
    if not done_oppose and not done_combine:
      el_list.append(inv)

  print "Case #%d: %s" % (i, "["+", ".join(el_list)+"]")

import sys
lines = sys.stdin.readlines()
cases = lines.pop(0)
i = 1
for case in lines:
  task(i, case)
  i+=1
