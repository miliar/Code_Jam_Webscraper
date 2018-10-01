#!/usr/bin/python2.6

class Inode:
    def __init__(self, name="", children=[]):
        self.name = name
        self.children = children

    def __str__(self, level=0):
        tabs = "\t"*level
        s = tabs + self.name + "\n"
        for child in self.children:
            if child == self:
                raise Exception("Self added: parent = %s, child = %s" % (self.name, child.name))
            s += "%s%s\in" % (tabs, child.__str__(level+1) )
        return s


hash = {}
root = Inode()
hash[""] = root

def add_dir1(dir):
    this_key = "/".join(dir)
    if this_key in hash:
        return

    parent_key = "/".join(dir[:-1])
    name = dir[-1]

    print("\tAdding: %s, name = %s, parent_key = %s, key = %s, hash = %s" % (dir, name, parent_key, this_key, hash) )

    if parent_key not in hash:
        add_dir(dir[:-1])

    parent_node = hash[parent_key]

    node = Inode(name)

    if node == parent_node:
        raise Exception("About to add parent to child")
    parent_node.children.append(node)
    hash[this_key] =  node


files = set()
mini = 0
def add_dir(dir):
    global mini
    if "/".join(dir) in files:
        return

    if "/".join(dir[:-1]) not in files:
        add_dir(dir[:-1])
    mini += 1
    files.add("/".join(dir))


def mkdirsNeeded(case, haves, needed):
    global mini
    files.clear()
    files.add("")

    given_dirs =  sorted(map(lambda x : x.split("/"), haves), key=lambda x: len(x), reverse=True)
    needed_dirs = sorted(map(lambda x : x.split("/"), needed), key=lambda x : len(x), reverse=True)

#    print "\t%s" % given_dirs
#    print "\t%s" % needed_dirs

    for d in given_dirs:
        add_dir(d)

    total = 0
    for d in needed_dirs:
        mini = 0
        add_dir(d)
#        print("\tmini = %d" % mini)
        total += mini

    print "Case #%d: %d " % (case,total)
    #print("\t" + str(total))
    #print hash
    #print root

cases = int(raw_input())

for i in range(cases):
    num_haves, num_needed = map(lambda x: int(x.strip()), raw_input().split())
    #print("Have: %d, Needed: %d" % (num_haves, num_needed))

    haves = []
    for a in range(num_haves): haves.append(raw_input().strip())

    needed = []
    for b in range(num_needed): needed.append(raw_input().strip())


    mkdirsNeeded(i+1, haves, needed)

