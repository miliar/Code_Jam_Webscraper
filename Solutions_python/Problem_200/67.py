
def solve():
  N = int(input())
  S = str(N)

  S = '0' + S

  last_val = '0'
  last_index = 0

  for i in range(1, len(S)):
    if S[i] > S[i-1]:
      last_val = S[i]
      last_index = i
    elif S[i] < S[i-1]:
      prefix = S[1:last_index]
      middle = chr(ord(S[last_index]) - 1)
      suffix = (len(S) - 1 - last_index) * '9'
      #middle = chr(ord(S[i-1]) - 1) + S[i-1] * (i - 1 - last_index)
      #middle = chr(ord(S[i-1]) - 1) * (i - 1 - last_index + 1)
      #suffix = (len(S) - 1 - i + 1) * '9'
      #print (prefix, middle, suffix)
      return int(prefix + middle + suffix)

  default = '9' * (len(S) - 2)
  #print ("default", default)
  if not default:
    default = '0'

  return max(N, int(default))

if __name__ == "__main__":
  T = int(input())
  for t in range(1, T + 1):
    solution = solve()
    print ("Case #{}: {}".format(t, solution))
