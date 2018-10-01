def attempt(n, m):
    flips=0
    while len(n)>=m:
        if n[0]=='-':
            flips+=1
            n = ''.join(['-' if e == '+' else '+' for e in n[1:m]]) + n[m:]
        else:
            n = n[1:]
    if len(n)<m:
        if n != len(n)*'+':
            return 'IMPOSSIBLE'
        else:
            return flips
t = int(input())
for i in range(1, t + 1):
  n, m = [s for s in input().split(" ")]
  print("Case #{}: {}".format(i, attempt(n, int(m))))
