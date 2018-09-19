#!/usr/bin/env python

import os, sys, re

def read_testcases(testlines, infile, extra_lines, extra_lines_ext):
    firstline = True
    curcase_testlines = testlines
    had_extra_lines = False
    total_cases = 0
    num_cases = 0
    cur_case = []
    testcases = []
    for line in infile:
        if firstline:
            total_cases = int(line)
            firstline = False
            continue
        cur_case.append(line)
        if len(cur_case) == curcase_testlines:
            if extra_lines_ext and not had_extra_lines:
                (curcase_testlines, had_extra_lines) = extra_lines_ext(cur_case)
            elif extra_lines and not had_extra_lines:
                curcase_testlines += extra_lines(cur_case)
                had_extra_lines = True
            if len(cur_case) == curcase_testlines:
                testcases.append(cur_case)
                curcase_testlines = testlines
                had_extra_lines = False
                num_cases += 1
                cur_case = []
    if len(cur_case) > 0:
        raise RuntimeError, "Oops, we had leftover data!"
    if num_cases != total_cases:
        raise RuntimeError, "Oops, we got %d testcases instead of %d!" % (num_cases, total_cases)
    return testcases

def main(args, runfn, testlines, by_dict=False, extra_lines=None, extra_lines_ext=None):
    infile = sys.stdin
    outfile = sys.stdout
    if len(args)>0:
        infile = open(args[0],"r")
        if len(args)>1:
            outfile = open(args[1],"w")
        else:
            outfilename = re.sub(".in",".out",args[0])
            if outfilename == args[0]:
                outfilename = args[0]+".out"
            outfile = open(outfilename,"w")
    testcases = read_testcases(testlines, infile, extra_lines, extra_lines_ext)
    infile.close()
    if by_dict:
        outdict = runfn(testcases)
        for i in range(len(testcases)):
            if i not in outdict:
                raise RuntimeError, "Oops, no test case returned for %d!" % i
            print >>outfile, "Case #%d: %s" % (i+1, str(outdict[i]))
    else:
        for i in range(len(testcases)):
            outcase = runfn(testcases[i])
            print >>outfile, "Case #%d: %s" % (i+1, str(outcase))
    outfile.close()

if __name__ == "__main__":
    main(sys.argv[1:], storecredit, 3)
