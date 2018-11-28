#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int d(int x,int y,int a,int b)
{
  return (x-a)*(x-a)+(y-b)*(y-b);
}

int main()
{
  int T,c;
  cin>>T;
  for(c=1;c<=T;c++)
    {
      int i,mx=0,n,x[3],y[3],r[3];
      double d1,d2,d3,t1,t2;
      cin>>n;
      cout<<"Case #"<<c<<": ";
      for(i=0;i<n;i++)
	{
	  cin>>x[i]>>y[i]>>r[i];
	  if(r[i]>mx)
	    mx=r[i];
	}
      if(n<3)
	t1=mx;
      else
	{
	  d1=sqrt(d(x[0],y[0],x[1],y[1]));
	  d2=sqrt(d(x[0],y[0],x[2],y[2]));
	  d3=sqrt(d(x[1],y[1],x[2],y[2]));
	  
	  t1=(d1+r[0]+r[1]>r[2])?d1+r[0]+r[1]:r[2];
	  t2=(d2+r[0]+r[2]>r[1])?d2+r[0]+r[2]:r[1];
	  if(t2<t1)
	    t1=t2;
	  t2=(d3+r[2]+r[1]>r[0])?d3+r[1]+r[2]:r[0];
	  if(t2<t1)
	    t1=t2;
	  t1/=2.0;
	}
      cout<<t1<<"\n";
    }
}
