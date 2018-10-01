#!/usr/bin/env python2.5

"""
universe.py
Google Code Jam 208
Solution for the "Saving the Universe" problem.
rbp@isnomore.net

For each engine, we list the indexes of each query. They are then
ordered from the highest to the lowest first occurrence, with no
occurrences at all coming first.

We start with the first engine in the (sorted) list. We then go
through the queries, marking switches and deleting each index from the
appropriate engine as it's read, and re-sorting. We stop when there's
an engine with no more occurrences (meaning the next switch will be to
it, and there will be no more switches needed).

Usage: universe.py input_file output_file
"""

import sys

def read_input():
    in_file = file(sys.argv[1])

    in_text = in_file.readlines()
    n_cases = int(in_text.pop(0))
    cases = []
    for i in range(n_cases):
        n_engines = int(in_text.pop(0))
        cases.append({'engines': [in_text.pop(0).strip()
                                  for j in range(n_engines)]})
        n_queries = int(in_text.pop(0))
        cases[-1].update({'queries': [in_text.pop(0).strip()
                                      for j in range(n_queries)]})
    in_file.close()
    return cases

def sort_by_first(a, b):
    # Lowest to highest, missing element is lowest.
    a_first = a[1][0] if a[1] else None
    b_first = b[1][0] if b[1] else None
    if a_first is None:
        return 1
    if b_first is None:
        return -1
    return cmp(a_first, b_first)

def solve_case(c):
    oc_dict = dict((e, list()) for e in c['engines'])
    for i, q in enumerate(c['queries']):
        oc_dict[q.strip()].append(i)
    occurrences = [list(i) for i in oc_dict.items()]
    occurrences.sort(cmp=sort_by_first, reverse=True)
    pos = dict((occurrences[i][0], i) for i in range(len(occurrences)))
    
    switches = 0
    cur_engine = occurrences[0][0]
    for q in c['queries']:
        if cur_engine == q:
            switches += 1
            cur_engine = occurrences[0][0]

        occurrences[pos[q]][1].pop(0)
        # Ugh! FIXME for real world: re-position only this element
        occurrences.sort(cmp=sort_by_first, reverse=True)
        pos = dict((occurrences[i][0], i) for i in range(len(occurrences)))

        if not occurrences[pos[cur_engine]][1]:
            break


    return switches

if __name__ == '__main__':
    cases = read_input()
    out_file = file(sys.argv[2], "w")
    output = "\n".join(['Case #%d: %d' % (i+1, solve_case(c))
                        for i, c in enumerate(cases)])
    out_file.write(output)
    out_file.close()
