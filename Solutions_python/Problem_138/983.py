def deceitful_war(n, naomi, ken):
  naomi.sort()
  ken.sort()
  visit, score = [False] * n, 0

  while ken:
    for i in xrange(n):
      if not visit[i] and naomi[i] > ken[-1]:
        score += 1
        visit[i] = True
        break
    ken = ken[:-1]

  return score

def war(n, naomi, ken):
  ken.sort()
  visit, score = [False] * n, 0

  for x in naomi:
    for i in xrange(n):
      if not visit[i] and ken[i] > x:
        visit[i] = True
        break
    else:
      score += 1

  return score

if __name__ == '__main__':
  T = input()

  for case in xrange(1, T+1):
    n = input()
    naomi = [float(x) for x in raw_input().split()]
    ken = [float(x) for x in raw_input().split()]

    print 'Case #{}: {} {}'.format(case, deceitful_war(n, naomi, ken), war(n, naomi, ken))