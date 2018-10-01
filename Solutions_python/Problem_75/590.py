#!/usr/bin/python
import sys

def do_prob(i, input):
   res = []
   comb = {}
   inputs = input.split()
   inputs.reverse()
   c = int(inputs.pop())
   for n in range(c):
      t = inputs.pop()
      comb[(t[0], t[1])] = t[2]
      comb[(t[1], t[0])] = t[2]
   exp = {}
   D = int(inputs.pop())
   for n in range(D):
      t = inputs.pop()
      exp[t[0]] = t[1]
      exp[t[1]] = t[0]
   inputs.pop()
   data = inputs.pop()
   for l in data:
       res.append(l)
       while len(res) > 1 and (res[-1], res[-2]) in comb:
         r = comb[(res[-1],res[-2])]
         if r == "":
	    res = []
         else:
	    res = res[:-2]
	    res.append(r)
       if res[-1] in exp:
          for l in exp[res[-1]]:
             if l in res:
                res = []
   
   print ("Case #%d: ["  + ", ".join(res) + "]")  % i
  
   
if __name__ == "__main__":
   input = open(sys.argv[1])
   num_inputs = int(input.readline())
   for i in range(num_inputs):
        do_prob(i+ 1, input.readline())

