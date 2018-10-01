import sys
fi=open(sys.argv[1],"r")
CASES=int(fi.readline())

for case in range(CASES):
  x,y=map(int,fi.readline().split())
  array=[]
  result=[]
  letter="a"
  for i in range(x):
    array.append(map(int,fi.readline().split()))
    result.append(len(array[-1])*[-1])
  for i in range(x):
    for j in range(y):
      ax=i
      ay=j
      while result[ax][ay]==-1:
        min=(0,0)
        min_val=0
        for xx,yy in [(-1,0),(0,-1),(0,1),(1,0)]:
          nx=xx+ax
          ny=yy+ay
          if nx>=0 and ny>=0 and nx<x and ny<y:
            if array[ax][ay]-array[nx][ny]>min_val:
              min=(nx,ny)
              min_val=array[ax][ay]-array[nx][ny]
        if min_val: ax,ay=min
        else:
          result[ax][ay]=letter
          if ord(letter)==255: letter=chr(40)
          else: letter=chr(ord(letter)+1)
          break
      
      l=result[ax][ay]
      ax=i
      ay=j
      while result[ax][ay]==-1:
        result[ax][ay]=l
        min=(0,0)
        min_val=0
        for xx,yy in [(-1,0),(0,-1),(0,1),(1,0)]:
          nx=xx+ax
          ny=yy+ay
          if nx>=0 and ny>=0 and nx<x and ny<y:
            if array[ax][ay]-array[nx][ny]>min_val:
              min=(nx,ny)
              min_val=array[ax][ay]-array[nx][ny]
  print "Case #%d:"%(case+1)
  for i in result: print " ".join(i)

fi.close()
