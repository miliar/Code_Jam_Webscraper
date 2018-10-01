import argparse
from math import ceil

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', help="input_file")
parser.add_argument('-o', '--output', help="output_file")
args = parser.parse_args()

O = 0
I = 1
J = 2
K = 3

M = {
  'i': I,
  'j': J,
  'k': K
}

DOTS = [
  [(1, O), (1, I), (1, J), (1, K)],
  [(1, I), (-1, O), (1, K), (-1, J)],
  [(1, J), (-1, K), (-1, O), (1, I)],
  [(1, K), (1, J), (-1, I), (-1, O)]
]

def dot(l, r, sign):
  sign2, res = DOTS[l][r]
  return(res, sign * sign2)

def dot_through(target, s, start, to_end=False):
  sign = 1
  v = O
  l = start
  while l < len(s):
    (v, sign) = dot(v, M[s[l]], sign)
    l += 1
    if (sign, v) == (1, target) and ((not to_end) or l >= len(s)):
      return l
  return None

def solve(data1, data2):
  l, x = int(data1[0]), int(data1[1])
  line = data2[0]
  assert len(line) == l
  s = line * x
  l = 0
  l = dot_through(I, s, l)
  if not l:
    return 'NO'
  l = dot_through(J, s, l)
  if not l:
    return 'NO'
  l = dot_through(K, s, l, True)
  if not l:
    return 'NO'
  return 'YES'
  

with open(args.input, 'r') as inf, open(args.output, 'w') as outf:
  n = int(inf.next())
  c = 0
  for line in inf:
    c += 1
    ans = solve(line.strip().split(), inf.next().strip().split())
    print >> outf, "Case #%s: %s" % (c, ans)
    n -= 1

assert n == 0
