import sys

class Directory:
	def __init__(self, name):
		self.name = name
		self.subdirs = []
	def create(self, path, createdCount=0):
		if len(path) > 0:
			exists = False
			i = 0
			while i < len(self.subdirs) and not exists:
				if self.subdirs[i].name == path[0]:
					exists = True
					return self.subdirs[i].create(path[1:], createdCount)
				i = i + 1
			if not exists:
				self.subdirs.append(Directory(path[0]))
				#print "New dir",path[0]
				createdCount = createdCount+1
				return self.subdirs[-1].create(path[1:], createdCount)
		else:
			return createdCount

def getMinMkdir(created, paths):
	count = 0
	root = Directory('root')
	for i in range(len(paths)):
		n = root.create(paths[i][1:].split('/'))
		if i > created-1:
			count = count + n
	return count

input = open(sys.argv[1])
output = open(sys.argv[2], 'w')

C = int(input.readline())
for i in range(C):
	line = input.readline().split()
	N = int(line[0])
	M = int(line[1])
	paths = []
	for j in range(N+M):
		line = input.readline()
		paths.append(line[:-1])
	output.write('Case #'+str(i+1)+': '+str(getMinMkdir(N, paths))+'\n')

input.close()
output.close()