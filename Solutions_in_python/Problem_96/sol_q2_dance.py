def inp(f_name = 'input.txt'):
  fin = open(f_name)
  t = int(fin.readline())
  inps = []
  for i in range(t):
     line = fin.readline()
     raw_ls = line.split()
     raw_ls_i = [int(x) for x in raw_ls]
     inp = (raw_ls_i[1], raw_ls_i[2], raw_ls_i[3:])
     inps.append(inp)
  fin.close()
  return inps

def out(res, f_name = 'out.txt'):
  fout = open(f_name, 'w')
  i = 1
  for r in res:
    tmp = 'Case #%d: %s\n' %(i, r)
    i += 1
    fout.write(tmp)
  fout.close()

def process(inps):
  res = []
  for inp in inps:
     rs = process_score(inp[2], inp[0], inp[1])
     res.append(rs)
  return res

def process_score(ls, s, mx):
   ls = sorted(ls)
   res = 0
   for n in ls:
     p, q = num_map[n]
     if q >= mx and s > 0:
 	res += 1
        s = s - 1
     elif p >= mx:
	res += 1
   return res
   


num_map = {0: (0,-1), 1 : (1,-1), 30: (10, -1)}
def get_map(n):
  p = n/3
  if n % 3 == 0: return p,  p + 1
  if n % 3 == 2: return p + 1, p + 2
  if n % 3 == 1: return p + 1, p + 1

for i in range(2,30):
   p, q = get_map(i)
   if p > 10: p = -1
   if q > 10: q = -1
   num_map[i] = (p, q)

	

def main():
  import sys
  fin_name = 'input.txt'
  fout_name = 'out.txt'
  try:
    fin_name = sys.argv[1]
    fout_name = sys.argv[2]
  except:
    pass
  inps = inp(fin_name)
  res = process(inps)
  out(res, fout_name)

if __name__ == '__main__':
  main()

