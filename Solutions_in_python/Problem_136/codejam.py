import sys

def read_word():
  x = sys.stdin.readline()
  return x.trim()

def read_word_list():
  x = sys.stdin.readline()
  return x.trim().split()

def read_int():
  x = sys.stdin.readline()
  return int(x)

def read_int_list():
  x = sys.stdin.readline()
  return map(int, x.split())

def read_float():
  x = sys.stdin.readline()
  return float(x)

def read_float_list():
  x = sys.stdin.readline()
  return map(float, x.split())
  
def main(ff):
  T = read_int()
  for t in xrange(1, T+1):
    print "Case #%d: %s" % (t, str(ff()))
