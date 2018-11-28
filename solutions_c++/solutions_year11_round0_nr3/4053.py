#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
  int t, n, c[100], i, tc, mval, temp, res=-1, xa, xb, sa, sb, j;
  cin>>t;
  for(tc=1;tc<=t;tc++)
  {
    res = -1;
    cin>>n;
    for(i=0;i<n;i++)
      cin>>c[i];
    mval = 1<<n;
    
    for(i=1;i<mval-1;i++)
    {
      xa = xb = sa = sb = 0;
      temp=i;
      for(j=0;j<n;j++)
      {
        if(temp&1)
        {
          xa ^= c[j];
          sa += c[j];
        }
        else
        {
          xb ^= c[j];
          sb += c[j];
        }
        temp = temp>>1;
      }
      if(xa==xb && max(sa,sb)>res)
        res = max(sa,sb);
    }
    if(res>-1)
      cout<<"Case #"<<tc<<": "<<res<<endl;
    else
      cout<<"Case #"<<tc<<": NO\n";
  }
}
