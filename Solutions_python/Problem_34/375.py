#!/usr/bin/python

import os
import sys
import math

def read_input_NN(fn =""):
  fh = open(fn, "r")
  lines = map(lambda x: x.strip(), fh.readlines())
  fh.close()
  [goog_L, goog_D, goog_N] = map(int, lines[0].split())
  l_dict = lines[1:1+goog_D]
  l_words = lines[1+goog_D:]
  return(l_dict, l_words)

def split_word(word1 = "(ab)c(ab)"):
  l1 = list(word1)
  in_paren = 0
  for (pos,letter) in enumerate(l1):
    if letter == "(":
      in_paren = 1
    elif letter == ")":
      in_paren = 0
    elif in_paren == 0:
      l1[pos]=","+letter
  return("".join(l1))

def qa(fn="sample"):
  l1 = read_input_NN(fn)
  solutions = []
  for i in l1[1]:
    word1 = split_word(i)
    final_words = l1[0]
    word1 = word1.replace("("," ").replace(")"," ").replace("  "," ").replace(","," ").replace("  "," ").strip()
    for (pos,letters) in enumerate(word1.split()):
      final_words = filter(lambda x: x[pos] in letters, final_words)
    solutions += [final_words]
  return(solutions)

l1 = qa(fn="A-large.in")
fh = open("out.txt","w")
for (ctr,sol) in enumerate(l1):
  print >> fh, "Case #"+str(ctr+1)+": "+str(len(sol))

fh.close()
