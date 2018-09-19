#! /usr/bin/env python
import sys

class Tree_Node:
  def __init__(self, weight):
    self.weight = weight
    self.feature = None
    self.node1 = None
    self.node2 = None

  def setFeature(self, feature):
    self.feature = feature

  def setChild(self, node):
    node.setParent(self)
    if self.node1 == None:
      self.node1 = node
    else:
      self.node2 = node

  def setParent(self, node):
    self.parent = node

  def getParent(self):
    return self.parent

  def getWeight(self):
    return self.weight

  def isLeaf(self):
    return self.feature == None

  def toString(self):
    if self.feature == None:
      return '(%f)' % self.weight
    else:
      return '(%f %s %s %s)' % (self.weight, self.feature, \
                                self.node1.toString(), self.node2.toString())

def createTree(tree_string, i, parent):
  num = tree_string[i]
  count_end = num.count(')')
  num = num.strip('()')
  if num == '':
    i += 1
    num = tree_string[i]
    count_end = num.count(')')
    num = num.strip('()')
  num = float(num)
  node = Tree_Node(num)
  parent.setChild(node)
  if count_end > 0:
    return [i,count_end]
  else:
    count_end = tree_string[i+1].count(')')
    if count_end > 0:
      return [i+1,count_end]
    node.setFeature(tree_string[i+1])
    temp = createTree(tree_string, i+2, node)
    temp = createTree(tree_string, temp[0]+1, node)
    if temp[1] > 1:
      return [temp[0],temp[1]-1]
    else:
      count_end = tree_string[temp[0]+1].count(')')
      return [temp[0]+1,count_end]

f_in = open(sys.argv[1], 'r')
f_out = open('%s.out' % sys.argv[1], 'w')

testcases = int(f_in.readline())

for k in range(testcases):
  treelines = int(f_in.readline())
  tree_root = None
  tree_string = []

  for i in range(treelines):
    string = f_in.readline()
    tree_string.extend(string.split())
    
  tree_root = Tree_Node(float(tree_string[0].strip('()')))
  if len(tree_string) > 1:
    tree_root.setFeature(tree_string[1])
    temp = createTree(tree_string, 2, tree_root)
    createTree(tree_string, temp[0]+1, tree_root)
    print tree_root.toString()

  print 'Case #%d:' % (k+1)
  f_out.write('Case #%d:\n' % (k+1))
  num_animal = int(f_in.readline())
  for m in range(num_animal):
    temp = f_in.readline()
    temp = temp.split()
    prob = 1.0
    tree_curr = tree_root
    prob *= tree_curr.getWeight()
    while not tree_curr.isLeaf():
      if tree_curr.feature in temp:
        tree_curr = tree_curr.node1
      else:
        tree_curr = tree_curr.node2
      prob *= tree_curr.getWeight()
    print '%.7f'%prob
    f_out.write('%.7f\n'%prob)
