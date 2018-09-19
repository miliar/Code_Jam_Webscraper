

def solve(r1, g1, r2, g2):
  sln = set(g1[r1 - 1]).intersection(set(g2[r2 - 1]))
  if len(sln) > 1:
    return 'Bad magician!'
  if len(sln) == 0:
    return 'Volunteer cheated!'
  return str(list(sln)[0])

with open('small_attempt.in', 'r') as fn:
  slns = []
  np = int(fn.readline())
  for j in range(np):
    r1 = int(fn.readline())
    g1 = [map(int, fn.readline().split(' ')) for _ in range(4)]
    r2 = int(fn.readline())
    g2 = [map(int, fn.readline().split(' ')) for _ in range(4)]
    slns.append(solve(r1, g1, r2, g2))
  with open('pa_small.out.csv', 'w') as fn:
    for i, sln in enumerate(slns):
      fn.write('Case #%d: %s\n' % (i + 1, sln))