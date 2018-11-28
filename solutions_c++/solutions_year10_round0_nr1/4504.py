#include<iostream.h>
#include<fstream.h>
#include<math.h>
void main()
{ int t,n,i,j,m,x,g=0;
  unsigned long int k;
  int a[30];
  int b[10000]={0};
  ifstream myfile;
  myfile.open("A.in");
  myfile>>t;
  for(i=0;i<t;i++)
  { for(j=0;j<30;j++)
    a[j]=0;
    x=0;
    myfile>>n;
    myfile>>k;
    for(j=0;j<n;j++)
    { for(m=pow(2,j)-1;m<k;m=m+pow(2,j))
      a[j]=!a[j];
    }
    for(j=0;j<n;j++)
    x=x+a[j];
    if(x==n)
    b[i]=1;
   }
    ofstream outf;
    outf.open("Out.in");
    for(i=0;i<t;i++)
    { if(b[i]==1)
      outf<<"Case #"<<i+1<<": "<<"ON\n";
      else
      outf<<"Case #"<<i+1<<": "<<"OFF\n";
    }
   myfile.close();
   outf.close();
}