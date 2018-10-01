def main():
  T = input()
  nonbases = set()
  bases = {}
  opposed = {}
  d={}
  for t in xrange(T):
    line = raw_input().split()
    opposed.clear()
    for c in 'QWERASDF':
      bases[c] = 0
    d.clear()
    C = int(line[0])

    for i in xrange(1,1+C):
      d[line[i][:2]] = line[i][2]
      d[line[i][:2][::-1]] = line[i][2]
    D = int(line[C+1])
    for i in xrange(2+C,2+C+D):
      opposed[line[i][0]] = line[i][1]
      opposed[line[i][1]] = line[i][0]
    N = int(line[2+C+D])
    a = line[3+C+D]
    out = []
    lastc = ''
    for c in a:
      if lastc+c in d:
        out.pop()
        out.append(d[lastc+c])
        bases[lastc] -= 1
        lastc = ''
      elif c in opposed and bases[opposed[c]]:
        out = []
        for x in 'QWERASDF':
          bases[x] = 0
        lastc = ''
      else:
        out.append(c)
        if c in 'QWERASDF':
          bases[c]+=1
        lastc = c
    print "Case #%d:"%(t+1),'['+', '.join(out)+']'
main()
