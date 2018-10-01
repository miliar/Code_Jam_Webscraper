#!/usr/bin/env python

cases = raw_input()
for c in range(int(cases)):
    (stack,k)=list(raw_input().split())
    k=int(k)  
    stack=list(stack)

    # lets just try a greedy approach
    flips = 0
    flip_from = None
    for i in range(0,len(stack)):
      if stack[i]=="+":
        continue
      else:
        #print "flipping!" 
        flips+=1
        if (len(stack)-i)<k:
          flips="IMPOSSIBLE"
          break
        else:
          for q in range(i,i+k):
            if stack[q]=="+":
               stack[q]="-"
            else: stack[q]="+" 
        
          
          
    a=str(flips)  
    print "Case #%i: %s" % ( (c+1), a)
