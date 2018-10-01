def find2(n):
  sm = 0
  pow2 = 1
  while n > sm:
    sm = pow2 + sm
    pow2 *= 2
  return (sm, pow2//2)
  
def sol(n, k):
  sm, pow2 = find2(k)
  val = (n-(sm-pow2))
  q = int(val/((sm-pow2)+1))
  a = val % pow2
  b = pow2 - a
  left = k - (pow2 - 1)
  if left <= a:
    #print(q+1)
    return(unpack(q+1))
  else:
    #print(q)
    return(unpack(q))
    
def unpack(i):
  if i % 2 == 0:
    return (i//2, i//2-1)
  else:
    return ((i-1)//2, (i-1)//2)


t = int(input())
for i in range(1, t + 1):
  n, k = [int(s) for s in input().split(" ")]
  a, b = sol(n, k)
  print("Case #{}: {} {}".format(i, a, b))
  

