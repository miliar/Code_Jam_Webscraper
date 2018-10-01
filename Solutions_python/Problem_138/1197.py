def line_to_int(line):
  return int(line.rstrip())

def closest_pair(universe):
  W = len(universe)
  for i in range(W):
    if i == W-1:
      return None

    if universe[i][1] == "N" and universe[i+1][1] == "K":
      return i

def closest_pair_inverse(universe):
  W = len(universe)
  for i in range(W):
    if i == W-1:
      return None

    if universe[i][1] == "K" and universe[i+1][1] == "N":
      return i

def playwar(N, naomi, ken):
  t_naomi = [ [ i, "N" ] for i in naomi ]
  t_len = [ [ i, "K" ] for i in ken ]

  universe = t_naomi + t_len
  sorted_universe = sorted(universe, key=lambda x: x[0])

  while True:
    pair_index = closest_pair(sorted_universe)

    if pair_index == None:
      break

    del sorted_universe[pair_index]
    del sorted_universe[pair_index]

  score = 0
  while True:
    pair_index = closest_pair_inverse(sorted_universe)
    if pair_index == None:
      break

    del sorted_universe[pair_index]
    del sorted_universe[pair_index]
    score += 1

  return score

def pick_worst_K(universe):
  W = len(universe)
  for i in range(W-1, -1, -1):
    if universe[i][1] == 'K':
      return i

def pick_best_N(universe):
  W = len(universe)
  for i in range(W):
    if universe[i][1] == 'N':
      return i

def play_deceitful_war(N, naomi, ken):
  t_naomi = [ [ i, "N" ] for i in naomi ]
  t_len = [ [ i, "K" ] for i in ken ]

  universe = t_naomi + t_len
  sorted_universe = sorted(universe, key=lambda x: x[0])

  scoreN = 0

  while True:
    # if element from the right side of the array is K than use the smallest
    # N element. Otherwise use the first N element that is located from right
    # to left.

    if len(sorted_universe) == 0:
      break

    candidate = sorted_universe[-1]
    if candidate[1] == 'N':
      position = pick_worst_K(sorted_universe)
      del sorted_universe[position]
      del sorted_universe[-1]

      scoreN += 1
    else:
      position = pick_best_N(sorted_universe)
      del sorted_universe[position]
      del sorted_universe[-1]

  return scoreN

def solve_case(fp, case_nb):
  N = line_to_int(fp.readline())
  naomi = [ float(i) for i in fp.readline().rstrip().split(" ") ]
  ken = [ float(i) for i in fp.readline().rstrip().split(" ") ]

  scoreWar = playwar(N, naomi, ken)
  scoreDWar = play_deceitful_war(N, naomi, ken)

  print "Case #%s: %s %s" % (case_nb+1, scoreDWar, scoreWar)

def solve():
  with open("D-large.in", "r") as fp:
    T = line_to_int(fp.readline())

    for i in range(T):
      solve_case(fp, i)

if __name__ == "__main__":
  solve()
