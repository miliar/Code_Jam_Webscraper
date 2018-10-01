import itertools
import collections

def try_chests(current_keys, chests, solution):
#  print(solution, sorted(chests))
  if not chests:
    yield list(solution)
  for i in sorted(chests):
#    print("considering chest %d" % i)
    Ti, Ki, contents = chests[i]
    if current_keys[Ti] > 0:
#      print("trying chest %d" % i)
      current_keys[Ti] -= 1
      current_keys.update(contents)
      del chests[i]
      solution.append(i)
      for s in try_chests(current_keys, chests, solution):
        yield s
      solution.pop()
      chests[i] = (Ti, Ki, contents)
      current_keys.subtract(contents)
      current_keys[Ti] += 1
      if current_keys[Ti] > 1 or Ti in contents or len(list(filter(lambda i: chests[i][0] == Ti, chests))) == 1:
        break

def solve(K, N, starting_keys, chests):
  current_keys = collections.Counter(starting_keys)
  for solution in try_chests(current_keys, chests, []):
    return " ".join(map(lambda i: str(i + 1), solution))
  return "IMPOSSIBLE"

def main():
  T = int(input())
  for case in range(1, T + 1):
    K, N = map(int, input().split())
    starting_keys = list(map(int, input().split()))
    chests = dict()
    for i in range(N):
      Ti, Ki, *contents = list(map(int, input().split()))
      chests[i] = (Ti, Ki, contents)
    print("Case #%d: %s" % (case, solve(K, N, starting_keys, chests)))
    
if __name__ == "__main__":
  main()

