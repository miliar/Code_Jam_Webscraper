import copy
import fractions
import os
import re
import string
import sys
import time

lookup = {
"i":"i",
"j":"j",
"k":"k",
"11":"1",
"1i":"i",
"1j":"j",
"1k":"k",
"i1":"i",
"ii":"-1",
"ij":"k",
"ik":"-j",
"j1":"j",
"ji":"-k",
"jj":"-1",
"jk":"i",
"k1":"k",
"ki":"j",
"kj":"-i",
"kk":"-1",
"-11":"-1",
"-1i":"-i",
"-1j":"-j",
"-1k":"-k",
"-i1":"-i",
"-ii":"1",
"-ij":"-k",
"-ik":"j",
"-j1":"-j",
"-ji":"k",
"-jj":"1",
"-jk":"-i",
"-k1":"-k",
"-ki":"-j",
"-kj":"i",
"-kk":"1",
"1-1":"-1",
"1-i":"-i",
"1-j":"-j",
"1-k":"-k",
"i-1":"-i",
"i-i":"1",
"i-j":"-k",
"i-k":"j",
"j-1":"-j",
"j-i":"k",
"j-j":"1",
"j-k":"-i",
"k-1":"-k",
"k-i":"-j",
"k-j":"i",
"k-k":"1",
}

def process(x, y):
   global found_i, found_j, found_k
   
   key = lookup[x+y]
   
   if (key == "i"): found_i = True
   if ((found_i == True) and (key == "k")): found_k = True
   
   return key
   
start = time.time()

filename = sys.argv[1]
file = open(filename, "rb")

cases = int(file.readline())
for case in range(1, cases+1):
   
   sys.stderr.write("%d\n" % (case))
   
   temp = file.readline().split()
   chars = int(temp[0])
   repeat = int(temp[1])
   pattern = list(string.strip(file.readline()) * repeat)
   
   found = False
   found_i = False
   found_j = False
   found_k = False
   found_ni = False
   found_nj = False
   found_nk = False

   product = reduce(lambda x,y: process(x, y), pattern, "")
   if ((found_k == True) and (product == "-1")):
         
      found = True
   
   # i_s = []
   # k_s = []
   
   # key = ""
   # for i in range(0, len(pattern)-2):
      # key = lookup[key + pattern[i]]
      # if (key == "i"):
         # i_s.append(i)
         
   # key = ""
   # for k in range(len(pattern)-1, 1, -1):
      # key = lookup[pattern[k] + key]
      # if (key == "k"):
         # k_s.append(k)
         
   # i = 0
   # while ((i < len(i_s)) and (found == False)):
   
      # k = 0
      # while ((k < len(k_s)) and (found == False)):
      
         # if (k_s[k] > i_s[i]):
      
            # start = i_s[i]+1
            # end = k_s[k]
            # if (reduce(lambda x,y: lookup[x+y], pattern[start:end], "") == "j"):
               # found = True
            
         # k += 1
         
      # i += 1
         
   if (found == False):
      print "Case #%d: NO" % (case)
   else:
      print "Case #%d: YES" % (case)
   
   #print (product, found_i, found_j, found_k, found_ni, found_nj, found_nk)
   
file.close()

end = time.time()

sys.stderr.write("%f\n" % (end-start))
