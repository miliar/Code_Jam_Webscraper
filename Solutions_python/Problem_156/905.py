from sys import argv
from math import ceil

MEMORY = {
  tuple([1]): 1,
  (1,1): 1,
  tuple([3]): 3,
  tuple([4]): 3,
  (2, 2): 2,
  (2, 2, 1): 2,
  (2, 2, 1, 1): 2
}  

def read_input(f):
  lines = open(f, 'r')
  T = int(lines.readline().strip())

  for i in xrange(T):
    N = int, lines.readline().strip()
    pancakes = map(int, lines.readline().strip().split(' '))

    yield i+1, N, pancakes
  lines.close()

def simulation(pancakes):
  cost = 0
  p_t = tuple(pancakes)
  #print p_t, MEMORY.get(p_t)
  if len(pancakes) > 0:
    if p_t in MEMORY:
      return MEMORY[p_t]
    
    m = pancakes[0]
    if m == 1:
      cost = 1
    else:
      normal_pancakes = filter(lambda x: x > 0, map(lambda x: x-1, pancakes))
      cost = simulation(normal_pancakes)

      for i in xrange(1, m / 2 + 1):
        special_pancakes = pancakes[:]
        special_pancakes[0] = i
        special_pancakes.append(m - i)
        #print "SPECIALS ", special_pancakes
        special_cost = simulation(sorted(filter(lambda x: x > 0, special_pancakes), reverse=True))
        if special_cost < cost:
          cost = special_cost

      #print "NORMAL ", normal_cost, "SPECIAL ", special_cost
      cost += 1
    
    #print p_t, cost
    MEMORY[p_t] = cost
    return cost
  else:
    return 0

if __name__ == '__main__':
  for test_case, _, pancakes in read_input(argv[1]):
    res = str(simulation(sorted(pancakes, reverse=True)))
    print "Case #%d: %s" % (test_case, res)