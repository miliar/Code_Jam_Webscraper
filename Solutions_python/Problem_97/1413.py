import os,sys
import itertools

def readlines(filename):
  input=open(filename,'r')
  googlers=[]
  l = input.readline()
  nl=int(l )
  for ii in range(nl):
    this_line = input.readline().split('\n')[0]
    keys = this_line.split()
    a =int(keys[0])
    b =int(keys[1])
    googlers.append( (a,b))
  return googlers

def get_recycle(a,b):
  count=0
  if(b<10): return 0
  if(b<100):
    for ii in range(a,b+1):
      if(ii%11==0): continue
      d1=int(ii/10)
      d2=ii-d1*10
      new_n = d2*10+d1
      if(new_n <= b and new_n >=a and new_n != ii):
        count=count+1
    return count
  if(b<1000):
    for ii in range(a,b+1):
      if(ii%111==0): continue
      d1=int(ii/10)
      d2=ii-d1*10
      new_n = d2*100+d1
      if(new_n <= b and new_n >=a and new_n != ii):
        count=count+1

      d1=int(ii/100)
      d2=ii-d1*100
      new_n = d2*10+d1
      if(new_n <= b and new_n >=a and new_n != ii):
        count=count+1
    return count

  if(b<10000):
    for ii in range(a,b+1):
      if(ii%1011==0): continue
      d1=int(ii/10)
      d2=ii-d1*10
      new_n = d2*1000+d1
      if(new_n <= b and new_n >=a and new_n != ii):
        count=count+1

      d1=int(ii/100)
      d2=ii-d1*100
      new_n = d2*100+d1
      if(new_n <= b and new_n >=a and new_n != ii):
        count=count+1

      d1=int(ii/1000)
      d2=ii-d1*1000
      new_n = d2*10+d1
      if(new_n <= b and new_n >=a and new_n != ii):
        count=count+1
    return count

  if(b<100000):
    return count
  if(b<1000000):
    return count
  if(b<10000000):
    return count

def run(args):
    filename = args[0]
    AB = readlines( filename )
    ii=1
    for a,b in AB:
      n=get_recycle(a,b)/2
      print "Case #%d: %d"%(ii, n )
      ii = ii + 1

if __name__ == "__main__":
  args=sys.argv[1:]
  run(args)
  
    
