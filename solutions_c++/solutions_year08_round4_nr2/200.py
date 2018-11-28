#include <iostream>
using namespace std;

int testNum,testCase;

int N,M,A;

int gcd (int a,int b,int &x,int &y)
{
  if (a%b==0)
  {
    x=0;
    y=1;
    return b;
  }
  else
  {
    int re=gcd(b,a%b,x,y);
    int t=x;
    x=y;
    y=t-(a/b)*y;
    return re;
  }
}

bool calc (int &x1,int &y1,int &x2,int &y2)
{
  for (x1=0;x1<=N;++x1)
    for (y1=0;y1<=M;++y1)
    {
      if (x1==0 || y1==0)
        continue;
      int g=gcd(x1,y1,y2,x2);
      if (A%g!=0)
        continue;
      //cout<<x2<<'*'<<y1<<'+'<<y2<<'*'<<x1<<'='<<g<<endl;
      x2*=A/g;
      int t1=x1/g;
      if (x2<0)
      {
        while (x2<0)
          x2+=t1;
        while (x2<=N)
        {
          y2=(A-x2*y1)/(-x1);
          if (y2>=0 && y2<=M)
            return true;
          x2+=t1;
        }
      }
      else if (x2>N)
      {
        while (x2>N)
          x2-=t1;
        while (x2>=0)
        {
          y2=(A-x2*y1)/(-x1);
          if (y2>=0 && y2<=M)
            return true;
          x2-=t1;
        }
      }
      else
      {
        int t=x2;
        while (x2<=N)
        {
          y2=(A-x2*y1)/(-x1);
          if (y2>=0 && y2<=M)
            return true;
          x2+=t1;
        }
        //cout<<"A"<<endl;
        x2=t;
        while (x2>=0)
        {
          y2=(A-x2*y1)/(-x1);
          if (y2>=0 && y2<=M)
            return true;
          x2-=t1;
        }
        //cout<<"B"<<endl;
      }
    }
  return false;
}

int main()
{
  cin>>testNum;
  for (testCase=1;testCase<=testNum;++testCase)
  {
    cin>>N>>M>>A;
    cout<<"Case #"<<testCase<<": ";
    if (A>N*M)
      cout<<"IMPOSSIBLE"<<endl;
    else
    {
      int x=-1,y=-1;
      for (int i=1;i<=N;++i)
        if (A%i==0 && A/i<=M && A/i>=0)
        {
          x=i;
          y=A/i;
          break;
        }
      if (x==-1 && y==-1)
      {
        int x1,y1,x2,y2;
        bool r1=calc(x1,y1,x2,y2);
        if (!r1)
          cout<<"IMPOSSIBLE"<<endl;
        else
          cout<<0<<' '<<0<<' '<<x1<<' '<<y1<<' '<<x2<<' '<<y2<<endl;
      }
      else
        cout<<0<<' '<<0<<' '<<x<<' '<<0<<' '<<0<<' '<<y<<endl;
    }
  }
}
