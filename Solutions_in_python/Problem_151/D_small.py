import itertools

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def num_nodes(words):
  prefixes = set([""])
  for w in words:
    for i in xrange(len(w)):
      prefixes.add(w[:i+1])
  return len(prefixes)

for cas in xrange(1, input()+1):
  print "Case #%d:" % cas,
  M, N = map(int, raw_input().split())
  words = []
  for _ in xrange(M):
    words.append(raw_input())
  arrangements = set()
  max_nodes = 0
  num_max = 0
  for divs in itertools.combinations(range(1, M), N-1):
    divs = list(divs) + [M]
    for ws in itertools.permutations(range(M)):
      arr_id = 0
      nodes = 0
      prev_div = 0
      for div in divs:
        arr_id *= 10**6
        set_words = []
        set_arr_id = 1
        for i in ws[prev_div:div]:
          set_arr_id *= primes[i]
          set_words.append(words[i])
        nodes += num_nodes(set_words)
        arr_id += set_arr_id
        prev_div = div
      if arr_id in arrangements:
        continue
      arrangements.add(arr_id)
      if nodes > max_nodes:
        max_nodes = nodes
        num_max = 1
      elif nodes == max_nodes:
        num_max += 1
  print max_nodes, num_max
