import sys

if __name__ == "__main__":
  data = open(sys.argv[1]).readlines()
  t = int(data[0])
  for i in range(1, t+1):
    inputs = data[i].split(" ")
    seq = list(inputs[0])
    k = int(inputs[1])
    ret = 0
    for j in range(len(seq)):
       if seq[j] == "-":
         ret += 1
         for p in range(k)[::-1]:
           if j + p >= len(seq):
             ret = -1
             break
           if seq[j+p] == "-":
             seq[j+p] = "+"
           else:
             seq[j+p] = "-"
    if ret == -1:
      print("Case #%d: IMPOSSIBLE" % i)
    else:
      print("Case #%d: %d" % (i, ret))
    

