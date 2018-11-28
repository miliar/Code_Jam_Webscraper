#include<iostream>
using namespace std;

int main()
{
  int t;
  cin >> t;
  for(int ti=1;ti<=t;++ti)
  {
    int c=0,n, s, p;
    cin >> n >> s >> p;
    while(n--)
    {
      int x,d,r;
      cin >> x;
      d=x/3, r=x%3;
      if(d>=p)
        ++c;
      else if(d==p-1)
      {
        if(r)
          ++c;
        else if(s&&d>0)
        {
          ++c,--s;
        }
      }
      else if(d==p-2)
        if(r==2&&s)
        {
          ++c,--s;
        }
    }
    cout << "Case #"<<ti<<": "<<c<<endl;
  }
}

      
