from Problem import Case, Problem

class FileParser:
  def __init__(self, config_lines, case_lines, path=None, fd=None):
    self.problem = None
    self.config_lines = config_lines
    self.case_lines = case_lines
    if fd:
      self._fd = fd
    elif path:
      self._fd = open(path, 'rb')

  def parse_problem(self):
    if not self.problem:
      config_args = []
      for i in xrange(self.config_lines):
        l = self._fd.readline()
        if len(l) > 0:
          config_args.append(l[:-1])
        else:
          raise Exception('Error: Encountered EOF when parsing problem.')
      if self._fd.name[-3:] == '.in':
        output_filename = self._fd.name[:-3]
      else:
        output_filename = self._fd.name
      writer = FileWriter(fd=open('%(output_filename)s.out' % locals(), 'wb'))
      self.problem = Problem(config_args, self, writer)
    else:
      print('Warning: Problem already parsed. Did not re-parse.')
    return self.problem

  def parse_case(self):
    nums = dict()
    if self.problem:
      case_args = []
      if self.case_lines == 'dynamic':
        l = self._fd.readline()
        if len(l) > 0:
          case_lines, case_length = map(int, l.split())
          case_args.append((case_lines, case_length))
        else:
          case_lines = 1
      else:
        case_lines = self.case_lines
      for i in xrange(case_lines):
        l = self._fd.readline()
        if len(l) > 0:
          case_args.append(l[:-1])
          rowarr = map(int, l.split())
          for num in rowarr:
            if nums.has_key(num):
              nums[num] += 1
            else:
              nums[num] = 1
        elif len(case_args) == 0:
          return None
        else:
          raise Exception('Encountered EOF while parsing case.')
      case_args.append(nums)
      return Case(case_args)
    else:
      raise Exception('Error: Problem not defined.')

  def close(self):
    if self._fd:
      self._fd.close()

class FileWriter:
  def __init__(self, path=None, fd=None):
    if fd:
      self._fd = fd
    elif path:
      self._fd = open(path, 'wb')

  def writeline(self, line):
    self._fd.write('%(line)s\n' % locals()) 

  def close(self):
    if self._fd:
      self._fd.close()
