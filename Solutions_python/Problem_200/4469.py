# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 21:02:03 2017

@author: ZENHU
"""
# N , numbers in N
def checkNum(N):
    N_num = 0
    a = 0
    b = 0
    c = 04
    if N>=100 and N<1000:
        N_num = 3
        a = N/100
        b = (N-a*100)/10
        c = N-100*a-10*b
    if N>=10 and N<100:
        N_num = 2
        a = 0
        b = N/10
        c = N-10*b
    if N>=1 and N<10:
        N_num = 1
        c = N
        a = 0
        b = 0
    return N_num,a,b,c
  
def my_program(m):
    N = m
    alist = []
    for i in range(1,N+1):
   
        Nn,a,b,c = checkNum(i)
        if Nn ==1:
            alist.append(i)
        if Nn ==2 and c>=b:
            alist.append(i)
        if Nn == 3 and c>=b and b>=a:
            alist.append(i)
    i_total = len(alist)
    return alist[i_total-1]

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  #n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  m = int(raw_input())
  m_new = my_program(m)
  
  
  
  
  
  
  print "Case #{}: {} ".format(i, m_new)
  # check out .format's specification for more formatting options


    