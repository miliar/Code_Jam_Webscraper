import sys
file=open(sys.argv[1])
T=int(file.readline())

#distinct pairs
#a hash table count is output
for i in range(T):
  recycle={};
  A,B=map(int,file.readline().split())
  if A<10:
    print 'Case #'+str(i+1)+': '+str(len(recycle))
    continue;

  for num in range(A,B):
      num_str=str(num)
      num_len=len(num_str)
      for n in range(1,num_len):
        if num < int(str(num_str[n:num_len])+str(num_str[0:n])) <=B:
          recycle[str(num)+str(num_str[n:num_len])+str(num_str[0:n])]=1

  print 'Case #'+str(i+1)+': '+str(len(recycle))




