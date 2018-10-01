file_in = open('A-large.in', 'r')
file_out = open('a.out', 'w')

T = int(file_in.readline())

combos = {
  2: [
    {1:2}
  ],
  3: [ 
    {1:1, 2:1},
    {1:3},
    {2:3}
  ],
  4: [
    {1:1, 3:1},
    {2:2},
    {1:2, 2:1},
    {2:1, 3:2},
    {1:4},
    {1:2, 3:2},
    {1:1, 2:2, 3:1},
    {2:4},
    {3:4}
  ]
}

def get_combos(p):
  if p not in combos:
    combos[p] = generate_combinations(p, p)
  return combos[p]

def generate_combinations(n, p, prune=True):
  # n = number of groups
  # p = number of pieces
  if n == 1:
    return [[i] for i in range(p)]
  combos = []
  for i in range(p):
    combos += [[i] + combo for combo in generate_combinations(n-1, p, False)]

  if prune:
    combos = [sorted(combo) for combo in combos if sum(combo) % p == 0]
    combos.sort()
    for i in range(1, len(combos)):
      if(combos[i] == combos[i-1]):
        combos[i-1] = None
    return [combo for combo in combos if combo is not None]
  else:
    return combos

for t in range(1, T+1):
  n, p = map(int, file_in.readline().split())
  groups = list(map(int, file_in.readline().split()))
  
  count = {}
  for group in groups:
    count[group%p] = count.get(group%p, 0) + 1
  ans = 0
  if 0 in count:
    ans += count.get(0, 0)
    del count[0]

  for combo in combos[p]:
    repeat = True
    while repeat:
      repeat = False
      for i in combo.keys():
        if combo[i] > count.get(i,0):
          break
      else:
        for i in combo.keys():
          count[i] -= combo[i]
        ans += 1
        repeat = True

  if sum(count.values()) > 0:
    ans += 1
    
  file_out.write("Case #{}: {}\n".format(t, ans))