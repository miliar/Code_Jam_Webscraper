class Node:
  def __init__(self, id, parent=None):
    self.id = id
    self.parent = parent

  def __cmp__(self, x):
    return 0 if self.id == x.id else 1

  def __repr__(self):
    return "<N:"+str(self.id)+">"

class UnionFind:
  def __init__(self, nodes):
    self.nodes = dict()
    for n in nodes:
      self.nodes[n] = Node(n)

  def find(self, id):
    node = self.nodes[id]
    if not node.parent:
      return node
    node.parent = self.find(node.parent.id)
    return node.parent

  def joined(self, x, y):
    return self.find(x) == self.find(y)

  def union(self, x, y):
    x = self.find( x )
    y = self.find( y )
    x.parent = y

  def clusters(self):
    return sum(1 for x in self.nodes if not self.nodes[x].parent)

if __name__=="__main__":
  from utils import dist
  pts = ((2,2,0),(2,3,0),(5,1,0),(7,16,0),(9,15,0),(9,16,0),(9,17,0))
  edges = []
  uf = UnionFind(pts)
  for i, x in enumerate(pts):
    for j, y in enumerate(pts[i+1:], i+1):
      edges.append( (dist(x,y), x, y) )

  edges.sort()

  msp = []
  while edges:
    d, x, y = edges.pop(0)
    print uf.clusters()
    if uf.joined(x, y):
      continue
    uf.union(x, y)
    msp.append( (d,x,y) )
  print msp
