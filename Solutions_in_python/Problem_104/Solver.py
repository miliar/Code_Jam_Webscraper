#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Apr 29, 2012

@author: daniel
'''

class Solver(object):
  def __init__(self, infile, outfile):
    with open(infile) as self.fhi, open(outfile, 'w') as self.fho:
      cases = int(self.fhi.readline())
      for case in range(1, cases + 1):
        self.solve(case)

  def solve(self, case):
    raise NotImplementedError('Sub-classes need to implement solve method.')

  def output(self, case, result):
    self.fho.write('Case #%d: %s\n' % (case, result))
