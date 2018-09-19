#! usr/bin/env python
import sys;

if __name__=='__main__':
  file=open(sys.argv[1],'r');
  text=file.readlines();
  file2=open(sys.argv[2],'r');
  text2=file2.readlines();
  for i in xrange(len(text2)):
    text2+=[text2[i][:-1]]
    print(text2[i])
  palin=[]
  palin2=[]
  for i in xrange(len(text)):
    palin+=[int(text[i][:-1])]
  for i in xrange(len(palin)):
    palin2+=[palin[i]**2]
  textw=""
  i=1;
  while(i<=int(text2[0])):
    s=text2[i].split();
    i=i+1;
    print(s)
    a=s[0];
    b=s[1];
    a=int(a);
    b=int(b);
    count=0;
    for j in xrange(len(palin2)):
      if(palin2[j]>=a and palin2[j]<=b):
        count=count+1;
    textw+="Case #"+str(i-1)+": "+str(count)+"\n";

  file3= open(sys.argv[3],'w+');
  file3.write(textw);
  file3.close();
  file.close();
  file.close();
