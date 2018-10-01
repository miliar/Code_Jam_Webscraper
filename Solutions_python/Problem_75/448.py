#! /usr/bin/python
import sys
import pprint
pp = pprint.PrettyPrinter(indent=4).pprint

class TailRecurseException:
  def __init__(self, args, kwargs):
    self.args = args
    self.kwargs = kwargs

def tail_call_optimized(g):
  """
  This function decorates a function with tail call
  optimization. It does this by throwing an exception
  if it is it's own grandparent, and catching such
  exceptions to fake the tail call optimization.
  
  This function fails if the decorated
  function recurses in a non-tail context.
  """
  def func(*args, **kwargs):
    f = sys._getframe()
    if f.f_back and f.f_back.f_back \
        and f.f_back.f_back.f_code == f.f_code:
      raise TailRecurseException(args, kwargs)
    else:
      while 1:
        try:
          return g(*args, **kwargs)
        except TailRecurseException, e:
          args = e.args
          kwargs = e.kwargs
  func.__doc__ = g.__doc__
  return func

## @tail_call_optimized

def uniq(list):
    seen = {}
    for x in list:
        seen[x] = 1 
    return seen.keys()

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    T = int(lines.pop(0))
    testcase = 1
    while testcase <= T:
        print "Case #%d:" % (testcase),

        base_nonbase_list = []
        oppose_list = []
        possible_oppose_elements = []

        test = lines.pop(0)
        testdata = test.split(" ")

        C = testdata.pop(0)
##         print "C = %s" % C
        for i in xrange(int(C)):
            base1, base2, nonbase = list(testdata.pop(0))
            base_nonbase_list.append((base1 + base2, nonbase))
            if base1 != base2:
                base_nonbase_list.append((base2 + base1, nonbase))
##         print "%s" % (base_nonbase_list)

        D = testdata.pop(0)
##         print "D = %s" % D
        for i in xrange(int(D)):
            base1, base2 = list(testdata.pop(0))
            oppose_list.append(base1 + base2)
            oppose_list.append(base2 + base1)
            possible_oppose_elements.extend([base1, base2])
        possible_oppose_elements = uniq(possible_oppose_elements)
##         print "%s" % (oppose_list)

        N = testdata.pop(0)
        inputs = list(testdata.pop(0).strip())

##         print "inputs = %s" % inputs
        testcase = testcase + 1


        def invoke():
            return inputs.pop(0)
        def combine(element):
            ret = False
            for base_set, nonbase in base_nonbase_list:
                if element_list[-1] + element == base_set:
                    ret  = nonbase
                    break
            return ret
        def oppose(invoked):
##             print "opposing %s with %s (oppose list = %s)" % (element_list, invoked, oppose_list)
            for el in element_list:
                if el + invoked in oppose_list:
                    return True
            return False
        def oppose2(invoked):
##             print "here with invoked: %s, list = %s, seen = %s" % (invoked, element_list, seen_oppose_elements)
            if invoked not in possible_oppose_elements:
                return False
            for el in seen_oppose_elements:
                if el + invoked in oppose_list:
                    return True
            seen_oppose_elements.append(invoked)
            return False

        element_list = []
        seen_oppose_elements = []
##         print inputs
        for i in xrange(len(inputs)):
            invoked = invoke()
##             print "SEQ: %s, invoked: %s" % (element_list, invoked)

            if len(element_list) < 1:
                if invoked in possible_oppose_elements:
                    seen_oppose_elements.append(invoked)
                element_list.append(invoked)
                continue

            nonbase = combine(invoked)
            if nonbase:
                last = element_list.pop()
                if last in seen_oppose_elements:
                    seen_oppose_elements.remove(last)
                element_list.append(nonbase)
##                 print "replace with %s" % nonbase
            elif oppose(invoked):
                element_list = []
                seen_oppose_elements = []
##                 print "cleared list"
            else:
                element_list.append(invoked)

        print "[%s]" % ", ".join(element_list)

if __name__ == '__main__':
    main()
