#!/usr/bin/python3
import sys
import functools as ft
import itertools as it
import argparse
from mushroom import solve

parser = argparse.ArgumentParser(description='C')
parser.add_argument('input_file',  type=argparse.FileType('r'))

def case(l1,l2):
  N = int(l1)
  snapshots = [int(i) for i in l2.split(' ')]
  return snapshots

def cases(lines):
  return (case(l1,l2) for l1,l2 in zip( *(iter(lines),)*2 ))

def main(input_file):
  lines = input_file.read().split('\n')
  number_of_cases = int(lines[0])
  for i,case in zip(range(1,number_of_cases+1), cases(lines[1:])):
    #print("Case #{}: {}".format(i, case))
    print("Case #{}: {} {}".format(i, *solve(case)))


if __name__ == "__main__":
  args = parser.parse_args()
  main(args.input_file)
