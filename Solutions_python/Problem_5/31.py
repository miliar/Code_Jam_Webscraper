import sys
#File=open('small.in');
File=sys.stdin;
g=sys.stdout
x=File.readline();C=int(x.strip());

def fSort(x,reverse=True):
    y=[];
    if not reverse:
      for i in range(len(x)):y.append([x[i],1*i])
    else:
      for i in range(len(x)):y.append([x[i],-1*i])
    y.sort(None,None,reverse);i=[];
    if not reverse:
      for [t1,t2] in y: i.append(t2)
    else:
      for [t1,t2] in y: i.append(t2*(-1))
    return i




for iC in range(1,C+1):
  t=File.readline().strip();N=int(t);
  t=File.readline().strip();M=int(t);
  A=[];
  for iM in range(M):
    t=File.readline().split();u=[];
    for t1 in t:u.append(int(t1));
    a=[];
    for i in range(1,len(u),2):a.append( (u[i],u[i+1]) );
    A.append(a);
  
  #sort
  t=[];
  for a in A:t.append(len(a));
  i=fSort(t,False);
  A1=[];
  for i1 in i:A1.append(A[i1]);
  A=A1;
  
 
  f=[];
  for i in range(N):f.append(-1);
  Queue=[f,[]];
  
  for iM in range(M):
  
    KQue={};
    #interperet
    while 1:
      f=Queue[0];del Queue[0];
      if len(f)==0:break; #end for this level
      #find all the possibile
      for iF in range(len(A[iM])):
        t=A[iM][iF];a1=t[0]-1;a2=t[1];
        if f[a1]==a2:
          f1=f[:]; tf1=tuple(f1);
          if not KQue.has_key(tf1):
            Queue.append(f1);KQue[tf1]=0;
          
        elif f[a1]==-1:
          f1=f[:]; f1[a1]=a2;tf1=tuple(f1);
          if not KQue.has_key(tf1):
            Queue.append(f1);KQue[tf1]=0;
        elif f[a1]!=a2:
          #abort
          tmp=-1;
    Queue.append([]);
  del Queue[-1]
  if Queue==[]:g.write('Case #%d: IMPOSSIBLE\n'%iC);
  else:#find min
    nMin=len(Queue[0])+1;qMin=[];
    for i in range(len(Queue)):
      t=Queue[i]; tn=sum(t);
      if tn<nMin:nMin=tn;qMin=t;
    g.write('Case #%d:'%iC);
    for t in qMin:
      if t==1:g.write(' 1');
      else:g.write(' 0');
    g.write('\n');
  
    
File.close();g.close();

    
    
    
  
  
  
