#include<iostream>
#include<cmath>
using namespace std;

int permute(int x,int d,int n)
{
  int p=pow(10,d);
  return x/p+x%p*pow(10,n-d);
}

int main()
{
  int t;
  cin >> t;
  for(int ti=1;ti<=t;++ti)
  {
    int a,b;
    cin >> a >> b;
    
    int x=a,n=0;
    while(x)
    {
      ++n;
      x/=10;
    }

    int r=0;
    for(int x=a;x<=b;++x)
      for(int d=1;d<n;++d)
      {
        int y=permute(x,d,n);
        if(x<y&&y<=b)
          ++r;
      }
    cout<<"Case #"<<ti<<": "<<r<<endl;
  }
}


    


