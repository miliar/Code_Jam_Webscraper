import sys

if __name__ == "__main__":
  data = open(sys.argv[1]).readlines()
  t = int(data[0])
  for i in range(1, t+1):
    [n, k] = [long(x) for x in data[i].split(" ")]
    count = long(1)
    while k > count:
      k -= count
      n -= count
      count *= 2
    if k <= (n%count):
      n = (n+count-1)/count
    else:
      n /= count
    l = n/2
    r = (n-1)/2
    print("Case #%d: %s %s" % (i, l, r))
