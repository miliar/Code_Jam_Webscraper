
class Manager(object):
  
    def __init__(self, file):
        self.mode = 'small' if 'small' in file else 'large'
        self.input = open(file, 'r')
        self.testcases = int(self.input.readline().strip())
        self.output = open('/home/ezequiel/Descargas/output_%s_%s' %(self.__class__.__name__, self.mode), 'w')
