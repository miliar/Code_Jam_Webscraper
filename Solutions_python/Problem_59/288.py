import sys

def run(f, N, M):
  existing = {}
  for i in range(0, N):
    l = f.readline().strip()
    l = l[1:]
    dirs = l.split('/')
    cur = existing
    for d in dirs:
      if not cur.has_key(d):
        cur[d] = {}
      cur = cur[d]
  count = 0
  # print existing
  for i in range(0, M):
    l = f.readline().strip()
    l = l[1:]
    dirs = l.split('/')
    cur = existing
    # print dirs
    for d in dirs:
      # print "checking: %s" % d
      if not cur.has_key(d):
        # print "  key not found"
        count += 1
        cur[d] = {}
      cur = cur[d]
  return count

if __name__ == "__main__":
  infile_n = sys.argv[1]
  infile = open(infile_n)
  T = int(infile.readline().strip())
  for i in range(0, T):
    (N, M) = infile.readline().strip().split(' ')
    print "Case #%d: %s" % (i + 1, run(infile, int(N), int(M)))


