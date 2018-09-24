#!/usr/bin/env python
# Google Code Jam 2008 Qualifcations, Task A
# Solution by Sebastian Hagen
# language: Python 2.5
# This program reads input from stdin and writes output to stdout.

class SwitchCounter:
   def __init__(self, se_count):
      self.se_count = se_count
      self.se_used = set()
      self.switch_count = 0
   
   def query_process(self, query):
      self.se_used.add(query)
      if (len(self.se_used) == self.se_count):
         self.se_used = set((query,))
         self.switch_count += 1
   
   @classmethod
   def build_from_file(cls, f):
      se_count = int(f.readline().strip())
      for i in range(se_count):
         f.readline() # don't need this data
      return cls(se_count)
   
   @classmethod
   def solve_from_file(cls, f):
      sc = cls.build_from_file(f)
      query_count = int(f.readline().strip())
      for i in range(query_count):
         sc.query_process(f.readline().strip('\r\n'))
      
      return sc.switch_count


if (__name__ == '__main__'):
   import sys
   tc_count = int(sys.stdin.readline().strip())
   for i in range(tc_count):
      sys.stdout.write('Case #%d: %d\n' % (i+1, SwitchCounter.solve_from_file(sys.stdin)))
      

