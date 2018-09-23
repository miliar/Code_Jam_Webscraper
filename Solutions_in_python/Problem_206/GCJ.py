
# coding: utf-8

# In[2]:

import numpy as np
import itertools as it
import collections as col


# In[3]:

import sys
sys.setrecursionlimit(10000)


# In[4]:

import networkx as nx
import matplotlib.pyplot as plt


# In[1]:

def solve(*args):
    print(args)


# In[16]:

def solve(D,N,Horses):
    t = [float(D - x[0]) / x[1] for x in Horses]
    sp = max(t)
    return D/sp


# In[ ]:

print(solve(5,5))


# In[18]:

path = r'C:\Users\Shachar\Downloads\A-small-attempt0.in'

with open(path, 'r') as f, open(path[:-2]+'out', 'w') as outf:
    T = int(f.readline())
    for test_index in range(T):
        D,N = [int(x) for x in f.readline().strip().split()]
        Horses = [ [int(x) for x in f.readline().strip().split()] for _ in range(N)]
        outf.write('Case #{}: {}\n'.format(test_index+1, solve(D,N,Horses)))

