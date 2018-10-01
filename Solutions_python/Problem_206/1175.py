def solve(D, N, K, S):
  # K is position
  # S is speed
  maxHour = (D - K[0]) / S[0] * 1.0
  for i in xrange(1, N):
    maxHour = max(
      maxHour,
      (D - K[i])/ S[i]
    )
  return round(D * 1.0 / maxHour, 6)


if __name__ == "__main__":
  T = input()
  for t in xrange(1, T + 1):
    D, N = map(int, raw_input().split(" "))
    K = []
    S = []
    for _ in xrange(N):
      hey = map(float, raw_input().split(" "))
      K.append(hey[0])
      S.append(hey[1])
    print "Case #" + str(t) +": " + "{0:.6f}".format(solve(D, N, K, S))
