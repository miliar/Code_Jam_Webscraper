
class CodeJamRunner(object):

    tests = 0
    results = None

    def __init__(self, filename):
        self.results = []
        self.tests = 0

        with open(filename, 'r') as f:
            self.tests = int(f.readline())
            for _ in xrange(self.tests):
                params = self.read_test(f)
                result = self.execute(**params)
                # print "Case #%s: %s" % ((_+1), result)
                self.results.append(result)

    def read_test(self, f):
        raise NotImplementedError()

    def execute(self, *args, **kwargs):
        raise NotImplementedError()

    def print_result(self):
        for (i, result) in enumerate(self.results):
            print "Case #%s: %s" % ((i+1), result)
