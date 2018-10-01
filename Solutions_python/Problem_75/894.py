import sys

def solve(line):
  l = line.split()
  C = int(l.pop(0))
  tr = dict(map(lambda x: (frozenset(x[:2]), x[-1]), l[:C]))
  l = l[C:]
  D = int(l.pop(0))

  op = {}

  for o in l[:D]:
    try:
      op[o[0]].add(o[1])
    except KeyError:
      op[o[0]] = set([o[1]])

    try:
      op[o[1]].add(o[0])
    except KeyError:
      op[o[1]] = set([o[0]])

  entry = l[-1]

  r = []

  for c in entry:
    if len(r) >= 1:
      base = frozenset(r[-1] + c)
      try:
        r[-1] = tr[base]
      except KeyError:
        r.append(c)

      try:
        if not op[r[-1]].isdisjoint(set(r[:-1])):
          r = []
      except KeyError:
        pass
    else:
      r.append(c)
  return r

def main(filename):
  f = open(filename, "r")

  T = f.readline()

  case = 1
  for line in f:
    print "Case #" + str(case) + ":",

    s = str(solve(line))
    print s.replace("'", "")


    case += 1

if __name__ == "__main__":
  main(sys.argv[1])
