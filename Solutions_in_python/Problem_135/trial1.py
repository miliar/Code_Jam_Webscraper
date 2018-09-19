'''
Created on 12-Apr-2014

@author: Hp-8
'''
#!/usr/local/bin/python2.7
    
f = open("input.txt","r");
ctr = int(f.readline())
k=1
out = open("output.txt","w")
print ctr
while(k<=ctr):
  p = []
  q = []
  row = int(f.readline())
  for i in range(4):
    a = f.readline().split()
    if (i+1) == row:
      for j in range(4):
        p.append(int(a[j]))

  row = int(f.readline())
  for i in range(4):    
    b = f.readline().split()
    if (i+1) == row:
      for j in range(4):
        q.append(int(b[j]))

  flag = 0
  for x in p:
    for y in q:
      if x==y:
        flag = flag+1;
        ans = x
  out.write('Case #%d: ' % k)
  if flag == 0:
    out.write('Volunteer cheated!\n')
  elif flag==1:
    out.write('%d\n'%ans)
  else:
    out.write('Bad magician!\n')
  k = k+1