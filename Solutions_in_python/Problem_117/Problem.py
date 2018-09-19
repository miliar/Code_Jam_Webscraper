class Case:
  def __init__(self, config):
    self.config = config

  def solve(self, logic):
    return logic(self.config)

class Problem:
  def __init__(self, config, parser, writer):
    self.case_counter = 0
    self.config = config
    self.parser = parser
    self.writer = writer
    self.case_logic = None
    self.solution_format = lambda x: 'Case #%i: %s' % (self.case_counter, x)

  def done(self):
    self.parser.close()
    self.writer.close()

  def next_case(self):
    rv = self.parser.parse_case()
    if rv:
      self.case_counter += 1
    return rv

  def solve(self):
    if self.case_logic and self.case_counter == 0:
      case = self.next_case()
      while case:
        solution = case.solve(self.case_logic)
        self.writer.writeline(self.solution_format(solution))
        case = self.next_case()
    elif not self.case_logic:
      raise Exception('Error: Logic not set')
    elif self.case_counter != 0:
      raise Exception('Error: Already solved')

  def set_case_logic(self, case_logic):
    self.case_logic = case_logic

  def set_solution_format(self, solution_format):
    self.solution_format = solution_format

