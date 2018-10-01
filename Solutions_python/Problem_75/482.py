#! /usr/bin/env python

import os
import sys
import math
import copy
import string
import numpy as np



def parse_line(l):
  comb = {};
  opp = dict.fromkeys(map(chr, range(ord('A'), ord('Z')+1)));
  for k in opp.keys():
    opp[k] = set();
  i = 0;

  nc = int(l[i]); 
  i += 1;
  for n in np.arange(nc):
    s = l[i+n];
    comb[s[:2]] = s[-1];
    comb[s[:2][::-1]] = s[-1];
  i += nc;

  no = int(l[i]); 
  i += 1;
  for n in np.arange(no):
    s = l[i+n];
    opp[s[0]].add(s[1]);
    opp[s[1]].add(s[0]);
  i += no;

  ni = int(l[i]); 
  i += 1;
  invoked = l[i];

  return (comb, opp, invoked);


def solve(comb, opp, invoked):
  l = [];

  for m in invoked:
    l.append(m);
    if len(l) < 2:
      # nothing to do
      continue;

    # can combine the last 2 elements?
    if string.join(l[-2:], '') in comb.keys():
      l[-2:] = comb[string.join(l[-2:], '')];

    # opposing elements?
    if len(opp[l[-1]].intersection(l[:-1])) > 0:
      # clear the list
      l = [];


  return l


if __name__=='__main__':
  f = open(sys.argv[1], 'r');
  T = int(f.readline());
  
  case = 0;
  for n in np.arange(T):
    case += 1;
    l = f.readline().split();
    (comb, opp, invoked) = parse_line(l);
    res = solve(comb, opp, invoked);

    rstr = 'Case #%d: %s' % (case, res)
    rstr = rstr.replace("'",'');
    print rstr


