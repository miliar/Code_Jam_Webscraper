import sys

def line(): return sys.stdin.readline().strip('\n')

def combine(st, combinations):
  if len(st) < 2: return st
  elems = st[-2:]
  elems2 = elems[1] + elems[0]
  for comb in combinations:
    if comb.startswith(elems) or comb.startswith(elems2):
      return st[:len(st)-2] + comb[2]
  return st

def checkoppos(final, oppossed):
  for ops in oppossed:
    if (final[-1:] == ops[0] and ops[1] in final) or (final[-1:] == ops[1] and ops[0] in final):
      return True
  return False

n = int(line())

for case in range(1, n+1):
  tmp = line().split(" ")
  c = int(tmp[0])
  tmp = tmp[1:]
  combinations = tmp[:c]
  tmp = tmp[c:]
  d = int(tmp[0])
  tmp = tmp[1:]
  oppossed = tmp[:d]
  tmp = tmp[d:]
  inp = tmp[1]
  
  final = ""
  for element in inp:
    final += element
    final2 = combine(final, combinations)
    if final <> final2:
      final = final2
    else:
      if checkoppos(final, oppossed):
        final = ""
  rst = "Case #" + str(case) + ": ["
  first = True
  for ch in final:
    if first: first = False
    else: rst += ', '
    rst += ch
  rst += "]"
  print rst
  
