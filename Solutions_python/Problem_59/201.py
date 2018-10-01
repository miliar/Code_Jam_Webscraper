class directory:
   def __init__(self, name):
      self.name = name      
      self.subdirs = {}

   def add_dir(self, name):
      self.subdirs[name] = directory(name)

for case in xrange(input()):
   n, m = [int(s) for s in raw_input().split()]
   dirs = [raw_input()[1:].split('/') for i in xrange(n)]
   newdirs = [raw_input()[1:].split('/') for i in xrange(m)]
   count = 0
   root = directory('root')
   for p in dirs:
      pwd = root
      for d in p:
         if not d in pwd.subdirs:
            pwd.add_dir(d)
         pwd = pwd.subdirs[d]

   for p in newdirs:
      pwd = root
      for d in p:
         if not d in pwd.subdirs:
            count += 1
            pwd.add_dir(d)
         pwd = pwd.subdirs[d]

   print 'Case #%d: %d' % (case+1, count)
