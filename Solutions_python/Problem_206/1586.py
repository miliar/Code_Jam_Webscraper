# Vendula Poncova

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

T = int(input())
for i in range(1, T + 1):

  D, N = (int(n) for n in input().split(" "))
  speed = 0
  max_time = 0

  for horse in range(1, N+1):
    Ki, Si = (int(n) for n in input().split(" "))
    v = float(Si)
    s = float(D - Ki)
    t = s / v

    if t > max_time:
      max_time = t


  speed = float(D) / max_time
  print("Case #{}: {:f}".format(i, speed))

