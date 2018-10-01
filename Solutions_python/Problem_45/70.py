from itertools import permutations

# end-n + n-start

cases = int(raw_input())
for i in xrange(cases):
  P, Q = map(int,raw_input().split())
  free = map(int, raw_input().split())
  cells = [0]*P
  for person in free:
    cells[person-1] = 1
  min_gold = -1
  for case in permutations(free):
    gold = 0
    freed = []
    for person in case:
      person -= 1
      a = person
      b = person
      freed.append(person)
      while (a-1) >= 0 and (a-1) not in freed:
        gold += 1
        a -= 1
      while (b+1) < P and (b+1) not in freed:
        gold += 1
        b += 1
    if min_gold == -1 or gold < min_gold:
      min_gold = gold

  print "Case #%d: %d" %(i+1, min_gold)

