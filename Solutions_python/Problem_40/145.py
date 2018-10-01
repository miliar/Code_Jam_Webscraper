#!/usr/bin/python

###############################################################################
#
# Google Code Jam 2009 - Round 1B : A
#
# Author: Andres Ayala
# email: killerrex@gmail.com
# License: GPL3
#
# Usage:
#   > qual.py input_file
#
#   input_file: File with the format specificated in the problem
#               No sanity checks are done over this files
#
###############################################################################

from sys import argv

class animal():
  def __init__(self, txt):
    """ Read the animal from the line"""
    txt = txt.split()
    self.name = txt[0]
    self.N = int(txt[1])
    self.prop = txt[2:]

class branch():
  """ Just one element of the tree from a list """
  def __init__(self, txt, pos = 0):

    pos +=1
    self.value = float(txt[pos])
    self.Elements = 3
    pos +=1
    if (txt[pos] == ')'):
      self.isleaf = True

    else:
      self.isleaf = False
      self.txt = txt[pos]
      pos +=1
      self.b1 = branch(txt, pos)
      pos += self.b1.Elements
      self.b2 = branch(txt, pos)
      self.Elements += self.b1.Elements + self.b2.Elements + 1
      
      
  def __str__(self):
    
    if self.isleaf:
      s = '(%.3f)' % self.value
    else:
      s = '(%.3f\t%s\n%s\n%s\n)' % (self.value, self.txt, str(self.b1),str(self.b2))
      
    return s

  def classify(self, animal):
    """ Main algo: Return the factor for this branch"""
    
    r = self.value
    if not self.isleaf:
      if self.txt in animal.prop:
        r *= self.b1.classify(animal)
      else:
        r *= self.b2.classify(animal)
    return r
    


def tree(fd):
  """
  Read a tree from the fd
  """
  
  L = int(fd.readline())
  
  s = ""
  for k in xrange(L):
    s += fd.readline()
  
  # Sanitize the input
  s = s.replace("(", " ( ").replace(")", " ) ")
  return branch(s.split())

  
def bestiary(fd):
  """
  Read all the animals from the file
  """
  L = int(fd.readline())
  an = L * [0]
  for k in xrange(L):
    an[k] = animal(fd.readline())
  return an
  
def batch(txt):
  """ Read the input and print the output :-D"""
  
  fd = open(txt,"r")  
  T = int(fd.readline())

  i=1
  for k in xrange(T):
    Tr = tree(fd)
    best = bestiary(fd)
    print "Case #%d:" % (k+1)
    for an in best:
      print "%9.7f" % Tr.classify(an)

  fd.close()
  

if len(argv)>1:
  batch(argv[1])

