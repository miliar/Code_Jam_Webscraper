
def add(v, k, n):
    try:
        v[k] += n
    except:
        v[k] = n

def solve(k,n):
    vals = {n : 1}
    while k > 0:
        z = max(vals.keys())
        v = vals[z]
        d2 = int(z/2)
        if v < k:
            k -= v
            del vals[z]
            assert z > 1

            if z % 2 == 0:
                add(vals, d2, v)
                add(vals, d2 - 1, v)
            else:
                add(vals, d2, 2 * v)
        else:
            if z % 2 == 0:
                return (d2 - 1, d2)
            else:
                return (d2, d2)

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n , k = [int(x) for x in input().split(" ")]

  (mn,mx) = solve(k, n)
  print("Case #{}: {} {}".format(i, int(mx), int(mn)))
  # check out .format's specification for more formatting options
