#include <iostream>

using namespace std;

int main()
{
  int N;
  cin>>N;
  for (int i=1;i<=N;i++)
  {
    long long a,b,c;
    cin>>a>>b>>c;
    bool u=0;
    if (b==0&&c==0)
      u=1;
    if (a>100)
      a=100;
    for (int i=1;i<=a;i++)
    {
      if ((i*b)%100==0)
        if (c<100&&c>0||(b==100)&&(c==100))
          u=1;
    }
    cout<<"Case #"<<i<<": ";
    if (u)
      cout<<"Possible\n";
    else
      cout<<"Broken\n";
  }
  return 0;
}

