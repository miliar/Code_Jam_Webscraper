import optparse
import os
import re
import pdb

class CodeJam(object):
  def __init__(self):
    self.init = 0
    self.filenames = []
    self.current_case = 0
    self.num_cases = 0
    self.input = 0
    self.output = 0

  def get_next_case(self):
    if self.current_case >= self.num_cases:
      if isinstance(self.input, file):
        self.input.close()
      if isinstance(self.output, file):
        print 'Closing output file'
        self.output.close()
      filename = self.get_next_filename()
      if filename == 0:
        print('No files')
        return 0
      print('Opening input file {0}'.format(filename))
      self.input = open(filename, 'r')
      self.num_cases = int(self.input.readline())
      self.current_case = 0
      self.output = open(''.join(['output_', filename, '.txt']), 'w')
    self.current_case += 1
    return self.input.readline()


  def get_filename_arg(self):
    p = optparse.OptionParser()
    opts, args = p.parse_args()
    assert(len(args) == 1)
    return args[0]


  def get_next_filename(self):
    if self.init == 0:
      self.init = 1
      for filename in os.listdir('.'):
        if re.search('^.*\.in$', filename):
          print filename
          self.filenames.append(filename)
    if self.filenames.__len__() == 0:
      return 0
    return self.filenames.pop(0)

  def output_current_case(self, output):
    self.output.write('Case {0}: {1}'.format(self.current_case, output))
      
    


