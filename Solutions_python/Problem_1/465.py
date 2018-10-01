import copy

#filename = 'unit.in'
#filename = 'A-small-attempt2.in'
filename = 'A-large.in'

debug = False

class Case(object):
    """Single case of the saving universe problem"""
    def __init__(self, filehandle):
        super(Case, self).__init__()
        self.filehandle = filehandle
        self.engines = []
        self.possible_current_engines = None
        self.switch_count = 0
        self.read_engines()
        self.read_queries()
        if self.switch_count < 0:
            self.switch_count = 0
                
    def read_engines(self):
        self.num_engines = int(self.filehandle.readline())
        for i in xrange(self.num_engines):
            self.engines.append(self.filehandle.readline().strip())
        self.reset_possible_engines()
        
    def read_queries(self):
        self.num_queries = int(self.filehandle.readline())
        for i in xrange(self.num_queries):
            query = self.filehandle.readline().strip()
            #if debug:
            #    print '"%s"  in  %s?\n%s' % (query, self.possible_current_engines, query in self.possible_current_engines)
            if query in self.possible_current_engines:
                self.possible_current_engines.remove(query)
                if len(self.possible_current_engines) < 1:
                    if debug:
                        print 'SWITCH (%s) (%s)' % (query, self.possible_current_engines)
                    self.switch_count += 1
                    self.reset_possible_engines(query)
                
    def reset_possible_engines(self, exception=None):
        """Resets the possible engines that can be chosen by the central
        query dispatch"""
        self.possible_current_engines = copy.deepcopy(self.engines)
        if exception:
            self.possible_current_engines.remove(exception)
            
        

class Environment(object):
    """The Universe that is filled with individual cases of our problem"""
    def __init__(self, filename):
        super(Environment, self).__init__()
        self.filename = filename
        self.filehandle = file(filename, 'r')
        self.current_engine = None
        self.cases = []
        self.read_cases()
    
    def read_cases(self):
        self.num_cases = int(self.filehandle.readline())
        for i in xrange(self.num_cases):
            case = Case(self.filehandle)
            print 'Case #%s: %s' % (i+1, case.switch_count)
            self.cases.append(case)

        
e = Environment(filename)