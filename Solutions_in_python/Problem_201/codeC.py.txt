# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  # check out .format's specification for more formatting options
  
  oldmax = n
  newmax = n
  
  if (n % 2 == 0):  
      l = n/2 - 1
      r = n/2
  else: 
      l = n/2 - 0.5 
      r = n/2 - 0.5
  
  
  maxval = max(l,r) #3
  minval = min(l,r) #2
  #print("FIRST - {} {}".format(maxval, minval))
  lister = [minval,maxval]
  
  for ii in range(1,m):
  
    if (lister[len(lister)-1] % 2 == 0):  
      l = lister[len(lister)-1]/2 - 1
      r = lister[len(lister)-1]/2
    else: 
      l = lister[len(lister)-1]/2 - 0.5
      r = lister[len(lister)-1]/2 - 0.5
    
    lister[len(lister)-1] = l
    lister.append(r)
    lister.sort()
    
    #print (lister)
    #print("{} - MAX {}  MIN {}  L {}  R{}".format(ii, maxval, minval, l, r))
    
    if (lister[len(lister)-1] == 0):
      #print("BREAK")
      break

  #print("{} {}".format(int(max(l,r)), int(min(l, r))))
  print("Case #{}: {} {}".format(i, int(max(l,r)), int(min(l,r))))
  
  