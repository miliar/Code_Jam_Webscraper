def addDirectory(dirs, newDir):
   mkdirs = 0
   localPoint = dirs
   newDir = newDir.split('/')
   newDir.pop(0)

   for path in newDir:
      if path in localPoint.keys():
         localPoint = localPoint[path]
      else:
         localPoint[path] = {}
         localPoint = localPoint[path]
         mkdirs += 1
   return mkdirs

data = open('A.in', 'r').read().split('\n')

T = int(data.pop(0))

for t in range(T):
   dirs = {}
   mkdirs = 0
   (N, M) = map(int, data.pop(0).split(' '))
   for i in range(N):
      addDirectory(dirs, data.pop(0))
   for i in range(M):
      mkdirs += addDirectory(dirs, data.pop(0))
   print 'Case #' + str(t+1) + ': ' + str(mkdirs)
