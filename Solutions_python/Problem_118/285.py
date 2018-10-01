fair_squares = []

def is_fair(n):
  return all(a == b for a,b in zip(str(n), reversed(str(n))))

def precompute_fair_squares():
  for i in range(1, 10 ** 7 + 1):
    if is_fair(i):
      i2 = i ** 2
      if is_fair(i2):
#        print(i2)
        fair_squares.append(i2)

def binary_search(x, is_upper_bound):
  a = 0
  b = len(fair_squares)
  while b - a > 1:
    c = (b + a) // 2
    if fair_squares[c] < x:
      a = c
    elif fair_squares[c] > x:
      b = c
    else:
      return c
  if fair_squares[a] == x:
    return a
  elif is_upper_bound:
    return a
  else:
    return b

def solve(A, B):
  lowest = binary_search(A, False)
  highest = binary_search(B, True)
#  print(lowest, highest)
  return highest - lowest + 1

def main():
  T = int(input())
  for case in range(1, T + 1):
    A, B = map(int, input().split())
    print("Case #%d: %s" % (case, solve(A, B)))

if __name__ == "__main__":
  precompute_fair_squares()
  main()
