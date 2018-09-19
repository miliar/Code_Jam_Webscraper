import sys, shlex, math

def nb_of_dancers_having(results, P):
  count = 0
  for i, dancer_results in enumerate(results):
    if max(dancer_results[1]) >= P:
      count += 1
  return count

def surprise_triplet(triplet, nb_surprising, P, force):
  res = False
  if (nb_surprising > 0) and ( ((max(triplet) + 1) == P) or (force == True and max(triplet) >= P) ):
    if (triplet[1] == triplet[2]) and (triplet[1] < 10) and (triplet[1] > 0):
      triplet[1] -= 1
      triplet[2] += 1
      res = True
    elif (triplet[0] == triplet[2]) and (triplet[0] < 10) and (triplet[0] > 0):
      triplet[0] -= 1
      triplet[2] += 1
      res = True
    elif (triplet[0] == triplet[1]) and (triplet[0] < 10) and (triplet[0] > 0):
      triplet[0] -= 1
      triplet[1] += 1
      res = True
  triplet.append(res)
  return triplet

def find_one_triplet(total_score):
  div = 3
  triplet = []
  while (div != 0):
    score = int(total_score / div)
    triplet.append(score)
    total_score -= score
    div -= 1
  return triplet

def find_triplets(tpts, nb_surprising, P):
  results = []
  tpts.sort()
  tpts.reverse()
  nbs = nb_surprising
  for i, total_score in enumerate(tpts):
    subres = []
    subres.append(total_score)
    triplet = surprise_triplet(find_one_triplet(total_score), nbs, P, False)
    subres.append(triplet[:-1])
    is_surprising = triplet[-1:][0]
    subres.append(is_surprising)
    if is_surprising == True:
      nbs -= 1
    results.append(subres)
  if nbs > 0:
    for i, dancer_results in enumerate(results):
      triplet = surprise_triplet(dancer_results[1], nbs, P, True)
      results[i][1] = triplet[:-1]
      is_surprising = triplet[-1:][0]
      results[i][2] = is_surprising
      if is_surprising == True:
        nbs -= 1
  return results

def dancingscores_decode(line):
  params = shlex.split(line)
  N = int(params[0])
  S = int(params[1])
  P = int(params[2])
  tpts = []
  for i in xrange(N):
    tpts.append(int(params[3+i]))
  return nb_of_dancers_having(find_triplets(tpts, S, P), P)

nblines = sys.stdin.readline()
for i in xrange(int(nblines)):
  line = sys.stdin.readline()
  resline = dancingscores_decode(line.rstrip('\r\n'))
  print "Case #%s: %s" % (str(i + 1), str(resline))