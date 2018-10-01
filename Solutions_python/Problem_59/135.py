class Fs:
  def __init__(self):
    self.root = {}
    self.added = 0

  def add(self, dir, skip_counting = False):
    l = dir[1:].split("/")
    pwd = self.root
    for part in l:
      if part not in pwd:
        pwd[part] = {}
        if not skip_counting:
          self.added += 1
      pwd = pwd[part]

if __name__ == "__main__":
  count = int(raw_input())
  for i in range(count):
    myfs = Fs()
    N, M = [int(s) for s in raw_input().split(" ")]
    for j in xrange(0, N):
      myfs.add(raw_input(), True)
    for j in xrange(0, M):
      myfs.add(raw_input())
    print 'Case #' + str(i+1)  + ': ' + str(myfs.added)
