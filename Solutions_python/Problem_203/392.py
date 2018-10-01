#!/usr/bin/env python

cases = raw_input()
ALPHA = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

for ca in range(int(cases)):
    (r,c) = raw_input().strip().split()
    r=int(r);c=int(c)
    cake = []
    for i in range(r):
      cake.append(list(raw_input().strip()))


    # i always just fill from left or right neighbors
    # if the row is completely empty, copy it up from below
    
    for i,r in enumerate(cake):
      if len(ALPHA.intersection(set(r))) == 0:
        if i!=0:
          r=cake[i-1]
        else: 
          k=1
          while len(ALPHA.intersection(set(r))) == 0:
            r=cake[i+k]
            k+=1
       
      # okay, we know that r isn't just empty
      if "?" in r:
        for j,c in enumerate(r): 
          # prefer copy from left 
          if c=="?":
            if j!=0:
              r[j]=r[j-1]
            else: 
              k=j+1
              for k in range(j+1,len(r)):
                if r[k] != "?":
                  r=r[0:j]+[r[k]]*(k-j)+r[k:]
                  break;

      cake[i]=r
          
      
    print "Case #%i:" % ( (ca+1))
    for r in cake:
      print "".join(r)
