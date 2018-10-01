# A.py - Oversized Pancake Flipper
# jreiter

for t in range(int(input())):
  s, k = input().split()
  s = list(s)
  k = int(k)
  flips = 0


  for i in range(len(s)):
    if s[i] == "-":
      if i > len(s) - k:
        flips = "IMPOSSIBLE"
        break

      for j in range(k):
        s[i+j] = "+" if s[i+j] == "-" else "-"

      flips += 1

  print("Case #{}: {}".format(t+1, flips))