#!/usr/bin/env python
# -*- coding: latin-1 -*-

#works with python 2.6.5
def set_existing_dir(line, current):
    stack = []
    subdirs = line.split('/')
    if subdirs:
        stack.append(subdirs)
    while stack:
        thedir = stack.pop()
        dirname = "".join(thedir)
        if not dirname:
            continue
        current["".join(thedir)] = 1
        more = thedir[:-1]
        if more:
            stack.append(more)

def main():
    total_cases = int(raw_input().strip())
    for case_number in range(1, total_cases+1):
        line = raw_input()
        existing, pending = map(int, line.split())
        #existing dirs
        current_dirs = {}
        total_created = 0
        for n in range(existing):
            line = raw_input().strip()
            set_existing_dir(line, current_dirs)
        old_dirs = len(current_dirs.keys())
        for m in range(pending):
            line = raw_input().strip()
            set_existing_dir(line, current_dirs)
        print "Case #%d: %d" % (case_number, len(current_dirs)-old_dirs)

if __name__ == '__main__':
    main()
