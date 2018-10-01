from operator import itemgetter
#iname, oname = "C-small-1-attempt0.in", "C-small-1-attempt0.res"
#iname, oname = "C-small-2-attempt0.in", "C-small-2-attempt0.res"
iname, oname = "C-large.in", "C-large.res"
with open(iname, 'r') as ifile, open(oname, 'w') as ofile:
  T = int(ifile.readline().strip())
  for t in range(T):
    n, k = map(int, ifile.readline().split())
    q = {n: 1}
    v1 = n
    v2 = n
    while k > 0:
      m = max(q)
      v = m - 1
      v2 = v // 2
      v1 = v - v2 
      q[v1] = q.get(v1, 0) + q[m]
      q[v2] = q.get(v2, 0) + q[m]
      k -= q[m]
      del q[m]
    print("Case #{}: {} {}".format(t+1, v1, v2), file = ofile) 
