#!/usr/bin/env python
import sys, os
from inspect import getargspec

class Break(Exception): pass
class IntList: pass
class StrList: pass

class ProblemBase(object):
    def __init__(self, fh):
        self._fh = fh
        aspec = getargspec(self.run_case)
        self.varvalts = zip(aspec.args[1:], aspec.defaults)

    def get_str(self):
        return self._fh.readline().strip()
    def get_int(self):
        return int(self.get_str())
    def get_strlist(self):
        return self.get_str().split()
    def get_intlist(self):
        return map(int, self.get_strlist())

    def print_result(self, case_no, result):
        print "Case #%i: %s" % (case_no, str(result))

    def run(self):
        self.N = self.get_int()
        for n in range(1, self.N+1):
            self._run_case(n)

    def _run_case(self, case_no):
        kw = {}
        for var, val in self.varvalts:
            if val == int:
                kw[var] = self.get_int()
            elif val == str:
                kw[var] = self.get_str()
            elif val == IntList:
                kw[var] = self.get_intlist()
            elif val == StrList:
                kw[var] = self.get_strlist()
            else:
                raise RuntimeError("Unknown method args specified on run_case method")

        self.print_result(case_no, self.run_case(**kw))


import numpy as np

class ProblemCase(ProblemBase):
    def run_case(self,
                 NM=IntList):

        N, M = NM
        pattern = np.zeros((N,M))
        doable = np.zeros((N,M))
        for i in range(N):
            pattern[i,:] = self.get_intlist()
            m = np.max(pattern[i,:])
            doable[i, pattern[i,:] == m] = 1

        for j in range(M):
            m = np.max(pattern[:,j])
            doable[pattern[:,j] == m, j] = 1

        if doable.all():
            return "YES"
        else:
            return "NO"


if __name__ == '__main__':

    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        cases = ProblemCase(open(sys.argv[1]))
    else:
        cases = ProblemCase(sys.stdin)

    cases.run()
