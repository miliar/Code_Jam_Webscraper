from collections import deque

def reverse(number):
  word = str(number)
  l = list(word)
  l.reverse()
  return int(''.join(l), 10)

def solve(N):
  frontier = deque([1])
  distance = {}
  distance[1] = 0

  while N not in distance and len(frontier) > 0:

    current = frontier.popleft()

    succ = current + 1
    if succ not in distance:
      distance[succ] = distance[current] + 1
      frontier.append(succ)

    reversed = reverse(current)
    if reversed not in distance:
      distance[reversed] = distance[current] + 1
      frontier.append(reversed)

  return 1 + distance[N]


if __name__ == '__main__':

  T = int(raw_input())

  for t in xrange(1,T+1):

    N = int(raw_input())
    print "Case #%d: %d" % (t, solve(N))

