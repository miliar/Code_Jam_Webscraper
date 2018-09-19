# Code Jam Utils
# Can be found on Github's Gist at:
# https://gist.github.com/Zren/5376385

from itertools import repeat
import logging
import json
import functools

LOGGING_FORMAT = "[%(asctime)s] %(message)s"
INFO = logging.INFO
DEBUG = logging.DEBUG

def log(a, b=None, level=logging.DEBUG):
    if b is None:
        msg = a
    else:
        msg = '%s: \t%s' % (a, b)
    logging.log(level, msg)

def info(a, b=None):
    log(a, b, logging.INFO)

def logdict(d, level=logging.DEBUG):
    logging.log(level, '\n' + json.dumps(d, indent=4))


# http://wiki.python.org/moin/PythonDecoratorLibrary#Alternate_memoize_as_nested_functions
# Does NOT memoize kwargs
def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer

class Problem(object):
    def __init__(self, id, size, filename=None, practice=False, log_level=INFO, attempt=None):
        self.id = id
        self.size = size
        self.filename = filename
        self.practice = practice
        self.attempt = attempt
        self.case = 1
        self.log_level = log_level

    def _filename(self):
        if self.filename is None:
            filename = "%s-%s" % (self.id, self.size)
            if self.practice:
                filename += "-practice"
            if not self.attempt is None:
                filename += "-" + str(self.attempt)
            return filename
        else:
            return self.filename
    def input_filename(self):
        filename = self._filename()
        filename += ".in"
        return filename

    def output_filename(self):
        filename = self._filename()
        filename += ".out"
        return filename

    def read_num_cases(self):
        self.num_cases = int(self.fin.readline())

    def writeline(self, line):
        log("Write", line)
        self.fout.write(line + '\n')

    def readline(self):
        line = self.fin.readline().rstrip('\n')
        log("Read", line)
        return line

    def readint(self):
        return int(self.readline())

    def readints(self):
        return map(int, self.readline().split())

    def writecase(self, s):
        self.writeline("Case #%d: %s" % (self.case, s))
        self.fout.flush()
        self.case += 1

    def __enter__(self):
        logging.basicConfig(level=self.log_level, format=LOGGING_FORMAT)

        info("=== Opening Streams ===")
        log("In", self.input_filename())
        log("Out", self.output_filename())
        self.fin = open(self.input_filename(), 'r')
        self.fout = open(self.output_filename(), 'w')

        self.read_num_cases()
        info("# of Cases", self.num_cases)

        return self

    def __exit__(self, type, value, traceback):
        self.fin.close()
        self.fout.close()

    def __len__(self):
        return self.num_cases

    def __getitem__(self):
        return self

    def __iter__(self):
        return repeat(self, len(self))

