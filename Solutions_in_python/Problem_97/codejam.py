#!/usr/bin/env python

import sys

class Case(object):
    def __init__(self, number, input):
        self.output = None
        self.input = input
        self.case_number = number
    
    def __unicode__(self):
        return 'Case #%s: %s' % (self.case_number, self.output)


class CodeJam(object):
    def __init__(self):
        in_file_path = sys.argv[1]
        file_ = open(in_file_path)
        
        self.cases = []
        self.n_cases = int(file_.readline())
        self.out_file_path = in_file_path.replace('.in', '.out')
        
        for i, line in enumerate(file_):
            self.cases.append(Case(i + 1, line))

        file_.close()

    def __call__(self, process_case_fnc):
        file_ = open(self.out_file_path, 'w')
        first = True

        for case in self.cases:
            if first:
                first = False
            else:
                file_.write('\n')

            case.output = process_case_fnc(case.input)
            file_.write(unicode(case))
        
        file_.close()
