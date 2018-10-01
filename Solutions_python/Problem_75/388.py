import sys

def hash(l):
  return "".join(sorted(l))

num_tests = int(sys.stdin.readline())
for test_num in range(1, num_tests + 1):
  vars = sys.stdin.readline().strip().split(" ")
  num_c = int(vars[0])
  c_list = vars[1 : num_c + 1]
  combine = {}
  oppose = set()
  for x in c_list:
    a, b, c = x
    combine[hash(sorted((a,b)))] = c
  num_d = int(vars[num_c + 1])
  d_list = vars[num_c + 2 : num_c + num_d + 2]
  for x in d_list:
    oppose.add(hash(x))
  num_e = int(vars[num_c + num_d + 2])
  e_list = vars[num_c + num_d + 3]
  assert(num_e == len(e_list))
  assert(num_c + num_d + 4 == len(vars))
  final = []
  for e in e_list:
    if final:
      h = hash(final[-1] + e)
      if h in combine:
        final[-1] = combine[h]
        continue
    final.append(e)
    for a in final:
      for b in final:
        if hash(a + b) in oppose:
          final = []
  print "Case #%d:" % test_num,
  print '[' + ", ".join(final) + ']'
