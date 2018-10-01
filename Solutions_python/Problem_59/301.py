#!/usr/bin/env python

import sys


class PathTree:
  def __init__(self):
    self.tree = {}

  def add(self, path):
    split_path = path.split("/")
    cur_node = self.tree
    create_count = 0
    for path in split_path:
      if len(path) > 0:
        if not path in cur_node:
          new_node = {}
          cur_node[path] = new_node
          cur_node = new_node
          create_count += 1
        else:
          cur_node = cur_node[path]
    return create_count

def main():
  t = int(sys.stdin.readline().strip())
  for i in xrange(0, t):
    path_tree = PathTree()
    split_line = sys.stdin.readline().split()
    n = int(split_line[0])
    m = int(split_line[1])
    count = 0
    # Read existing paths
    for j in xrange(0, n):
      line = sys.stdin.readline().strip()
      path_tree.add(line)
    # Get number of dirs needed to create all directories
    for j in xrange(0, m):
      line = sys.stdin.readline().strip()
      count += path_tree.add(line)
    print "Case #%d: %d" % (i+1, count)

if __name__ == "__main__":
  main()
