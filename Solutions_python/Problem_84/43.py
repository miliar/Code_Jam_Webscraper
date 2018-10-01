import sys

def solve(A, N, M):
  for i in range(N):
    for j in range(M):
      if A[i][j] == '.':
        continue
      if A[i][j] != '#':
        continue
      if i+1 < N and A[i+1][j] == '#' and \
        j+1 < M and A[i][j+1] == '#' and A[i+1][j+1] == '#':
          A[i][j] = '/'
          A[i+1][j] = '\\'
          A[i][j+1] = '\\'
          A[i+1][j+1] = '/'
      else:
        return False
  return True


def main(args):
  T = int(raw_input())
  for t in range(1, T+1):
    print "Case #%d:" % t
    N, M = map(int, raw_input().split())
    A = []
    for i in range(N):
      A.append(list(raw_input())[:M])
    if solve(A, N, M):
      for line in A:
        print ''.join(line)
    else:
      print "Impossible"

if __name__ == '__main__':
  main(sys.argv)
