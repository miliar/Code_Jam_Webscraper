import sys

if __name__ == "__main__":
  data = open(sys.argv[1]).readlines()
  t = int(data[0])
  idx = 1
  for i in range(1, t+1):
    [d, n] = [float(x) for x in data[idx].split(" ")]
    idx += 1
    max_t = None
    for j in range(int(n)):
      [k, s] = [float(x) for x in data[idx].split(" ")]
      idx += 1
      if max_t < (d-k)/s:
        max_t = (d-k)/s
    #ret = round(d/max_t, 6)
    ret = d / max_t
    print("Case #%d: %.6f" % (i, ret))
