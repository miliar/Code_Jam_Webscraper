
def solve():
  S, K = input().split()

  S = list(S)
  K = int(K)
  N = len(S)

  cnt = 0

  #print (S, N, K)

  for i in range(N):
    if i + K - 1 < N and S[i] == '-':
       cnt += 1
       for j in range(i, i + K):
          S[j] = '+' if S[j] == '-' else '-'
       #print (S)

  if S == ['+'] * N:
    return cnt
  return 'IMPOSSIBLE'
      

if __name__ == "__main__":
  T = int(input())
  for t in range(1, T + 1):
    solution = solve()
    print ("Case #{}: {}".format(t, solution))
