#include <iostream>
#include <iomanip>

using namespace std;

struct xd
{
  int a,b;
};

bool ss(xd a,xd b)
{
  return a.b<b.b;
}

int main()
{
  int N;
  cin>>N;
  cout.precision(10);
  for (int i=1;i<=N;i++)
  {
    cout<<"Case #"<<i<<": ";
    int a,b,c,e;
    double d;
    cin>>a>>b>>c>>d>>e;
    int x[e],y[e],z[e];
    int r=0;
    for (int i=0;i<e;i++)
    {
      cin>>x[i]>>y[i]>>z[i];
      r+=y[i]-x[i];
    }
    r=a-r;
    if (c*d<=r)
    {
      double t=d;
      r-=c*d;
      t+=r*1.0/b;
      for (int i=0;i<e;i++)
        t+=(y[i]-x[i])*1.0/(b+z[i]);
      cout<<t;
    }
    else
    {
      xd q[e];
      for (int i=0;i<e;i++)
      {
        q[i].a=y[i]-x[i];
        q[i].b=z[i];
      }
      sort(q,q+e,ss);
      double t=r*1.0/c;
      d-=t;
      for (int i=0;i<e;i++){//cout<<q[i].a<<' '<<q[i].b<<endl;
        if (d>0)
        {
          double g=d*(c+q[i].b);//can run this far
          if (g>=q[i].a)
          {
            double tt=q[i].a*1.0/(c+q[i].b);
            t+=tt;
            d-=tt;
           // cout<<tt<<endl;
          }
          else
          {
            double rd=q[i].a-g;
            double tt=g*1.0/(c+q[i].b)+rd*1.0/(b+q[i].b);
            d=0;
            t+=tt;
          }
          //cout<<d<<' '<<g<<endl;
        }
        else
          t+=q[i].a*1.0/(b+q[i].b);}
      cout<<t;
    }
    cout<<endl;
  }
  return 0;
}

