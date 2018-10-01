#!/usr/bin/python
import sys
sys.setrecursionlimit(1000000000)

def calc_mat(mat, N, L, a_i, t):
  if mat[N][L] is not None:
    return mat[N][L]

  if N == 0:
    mat[N][L] = 0
  elif L == 0:
    mat[N][L] = calc_mat(mat, N-1, L, a_i, t) + 2*a_i[(N-1)%len(a_i)]
  else:
    without = calc_mat(mat, N-1, L, a_i, t) + 2*a_i[(N-1)%len(a_i)]
    with_time = calc_mat(mat, N-1, L-1, a_i, t)
    if with_time >= t:
      withy = with_time + a_i[(N-1)%len(a_i)]
    else:
      time_left = (t-with_time)
      d = a_i[(N-1)%len(a_i)]
      if 2*d <= time_left:
        withy = with_time + 2*d
      else:
        withy = with_time + time_left + (d-(time_left/2))
    mat[N][L] = min(without, withy)
 
  return mat[N][L]

def calc(L,t,N,C,a_i):
  mat = []
  for i in xrange(N+1):
    mat.append([])
    for j in xrange(L+1):
      mat[-1].append(None)
  return calc_mat(mat, N, L, a_i, t)

def main(filename):
  f = file(filename)
  n = int(f.readline())
  for case in xrange(1, n+1):
    l = map(int, f.readline().split())
    print "Case #%d: %d" % (case, calc(l[0], l[1], l[2], l[3], l[4:]))

if __name__ == "__main__":
  main(sys.argv[1])
