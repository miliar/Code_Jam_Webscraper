#!/usr/bin/python

import sys
import math

def is_polindrom(s):
  s = str(s)
  for i in range(0, len(s) / 2):
    if s[i] != s[len(s) - i - 1]:
      return False
  return True

def count_numbers(A, B):
  pnumber = math.sqrt(A)
  while not pnumber.is_integer():
    pnumber = math.sqrt(A)
    A = A + 1
  pnumber = int(pnumber)
  number = A
  nums = []
  while number <= B:
    if is_polindrom(pnumber):
      if is_polindrom(number):
	nums.append(number)
    pnumber = pnumber + 1
    number = pnumber * pnumber
  print nums
  return len(nums)

def count_numbers_small(A, B):
    nums = [1, 4, 9, 121, 484]
    c = 0;
    for i in nums:
      if i >= A and i <= B:
	c = c + 1
    return c
  
def count_numbers_large(A, B):
    nums = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001, 100220141022001, 102012040210201, 102234363432201, 121000242000121, 121242363242121, 123212464212321, 123456787654321, 400000080000004]
    c = 0;
    for i in nums:
      if i >= A and i <= B:
	c = c + 1
    return c

T = int(sys.stdin.readline())
for iT in range(0, T):
  AB = sys.stdin.readline().split()
  A = int(AB[0])
  B = int(AB[1])
  print 'Case #' + str(iT + 1) + ':', count_numbers_large(A, B)